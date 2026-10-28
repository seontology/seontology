"""MkDocs hooks that turn the SEOntology guide into a site for humans and agents.

Besides the MkDocs pages, the build publishes:

- reference/       pyLODE HTML reference generated from seovoc.ttl, plus a
                   Markdown term index (reference/index.md)
- seovoc.ttl/.owl  copies of the generated ontology artifacts
- seovoc.jsonld    the ontology serialized as JSON-LD
- context.jsonld   a JSON-LD context mapping SEOntology terms to IRIs
- examples/        the example fixtures from the repository
- llms.txt         an index for LLM agents; llms-full.txt with all content
- <page>/index.md  the Markdown source of every guide page
"""

import json
import logging
import os
import re
import shutil
from pathlib import Path

from mkdocs.structure.files import File
from rdflib import BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, VANN, XSD

log = logging.getLogger("mkdocs.hooks.seontology")

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/seontology/seontology"
SEOVOC = Namespace("https://w3id.org/seovoc/")
ONTOLOGY = URIRef(str(SEOVOC))
DC = Namespace("http://purl.org/dc/elements/1.1/")
SCHEMA = Namespace("https://schema.org/")

# Markdown source of each rendered page, keyed by page URL in nav order.
_pages: dict[str, dict] = {}


def _rendered_pages():
    return [(url, page) for url, page in _pages.items() if page is not None]


def ontology_version(g: Graph) -> str:
    """The ontology's owl:versionInfo, falling back to the VERSION file."""
    env = os.environ.get("SEOVOC_VERSION")
    if env:
        return env.lstrip("v")
    return first(g, ONTOLOGY, OWL.versionInfo) or (ROOT / "VERSION").read_text().strip()


def load_ontology() -> Graph:
    return Graph().parse(ROOT / "seovoc.ttl")


def first(g: Graph, s, *preds):
    for p in preds:
        for o in g.objects(s, p):
            if isinstance(o, Literal):
                return str(o)
    return None


def curie(g: Graph, node) -> str:
    if isinstance(node, BNode):
        members = next(g.objects(node, OWL.unionOf), None)
        if members is not None:
            return " ∪ ".join(curie(g, m) for m in g.items(members))
        return "(anonymous)"
    if str(node).startswith(str(SEOVOC)):
        return "seovoc:" + str(node)[len(SEOVOC):]
    return g.namespace_manager.normalizeUri(node)


def seovoc_terms(g: Graph):
    """Yield (local name, kind, IRI) for every term in the seovoc namespace."""
    kinds = [
        (OWL.Class, "Class"),
        (OWL.ObjectProperty, "ObjectProperty"),
        (OWL.DatatypeProperty, "DatatypeProperty"),
        (OWL.AnnotationProperty, "AnnotationProperty"),
    ]
    for rdf_type, kind in kinds:
        for s in sorted(set(g.subjects(RDF.type, rdf_type)), key=str):
            if isinstance(s, URIRef) and str(s).startswith(str(SEOVOC)) and s != ONTOLOGY:
                yield str(s)[len(SEOVOC):], kind, s


def build_context(g: Graph) -> dict:
    """JSON-LD context: classes and properties by local name, typed where the
    ontology declares a single non-string range."""
    ctx: dict = {
        "@version": 1.1,
        "seovoc": str(SEOVOC),
        "schema": str(SCHEMA),
        "xsd": str(XSD),
    }
    for name, kind, iri in seovoc_terms(g):
        term = f"seovoc:{name}"
        if kind == "ObjectProperty":
            ctx[name] = {"@id": term, "@type": "@id"}
        elif kind == "DatatypeProperty":
            ranges = [r for r in g.objects(iri, RDFS.range) if isinstance(r, URIRef)]
            if len(ranges) == 1 and str(ranges[0]).startswith(str(XSD)) and ranges[0] != XSD.string:
                ctx[name] = {"@id": term, "@type": curie(g, ranges[0])}
            else:
                ctx[name] = term
        else:
            ctx[name] = term
    return {"@context": ctx}


def reference_markdown(g: Graph, version: str, site_url: str) -> str:
    """A compact term index for agents and llms-full.txt."""
    title = first(g, ONTOLOGY, DC.title, RDFS.label) or "SEOntology"
    lines = [
        f"# {title} reference (version {version})",
        "",
        "Namespace: `https://w3id.org/seovoc/` (prefix `seovoc:`).",
        f"HTML reference: {site_url}reference/",
        "",
    ]
    sections = {
        "Class": "Classes",
        "ObjectProperty": "Object properties",
        "DatatypeProperty": "Datatype properties",
        "AnnotationProperty": "Annotation properties",
    }
    by_kind: dict[str, list] = {k: [] for k in sections}
    for name, kind, iri in seovoc_terms(g):
        by_kind[kind].append((name, iri))
    for kind, heading in sections.items():
        lines += [f"## {heading}", ""]
        for name, iri in by_kind[kind]:
            label = first(g, iri, RDFS.label)
            desc = first(g, iri, DC.description, RDFS.comment)
            parts = [f"- **seovoc:{name}**"]
            if label and label != name:
                parts.append(f"({label})")
            if (iri, OWL.deprecated, Literal(True)) in g:
                parts.append("_deprecated_")
            if desc:
                parts.append("— " + " ".join(desc.split()))
            details = []
            supers = [curie(g, o) for o in g.objects(iri, RDFS.subClassOf) if isinstance(o, URIRef)]
            supers += [curie(g, o) for o in g.objects(iri, RDFS.subPropertyOf)]
            if supers:
                details.append("subOf " + ", ".join(sorted(supers)))
            domains = [curie(g, o) for o in g.objects(iri, RDFS.domain)]
            if domains:
                details.append("domain " + ", ".join(domains))
            ranges = [curie(g, o) for o in g.objects(iri, RDFS.range)]
            if ranges:
                details.append("range " + ", ".join(ranges))
            if details:
                parts.append(f"[{'; '.join(details)}]")
            lines.append(" ".join(parts))
        lines.append("")
    return "\n".join(lines)


def fix_anchors(html: str) -> str:
    """Give every seovoc term the fragment of its local name.

    pyLODE derives fragments from local names and de-duplicates them in
    document order, so seovoc:WebPage becomes #WebPage1 after schema:WebPage,
    and some names are lowercased. w3id redirects term IRIs to
    reference/#<local name>, so that fragment must belong to the seovoc term.
    """
    entities = re.findall(r'id="([^"]+)">\s*<h3>.*?IRI.*?<code>(https?://[^<]+)</code>', html, re.S)
    local_names = {
        iri[len(SEOVOC):] for _, iri in entities if iri.startswith(str(SEOVOC))
    }
    # Functional properties are listed twice; only one entry needs the anchor.
    anchored = {iri for fid, iri in entities if iri.startswith(str(SEOVOC)) and fid == iri[len(SEOVOC):]}
    mapping = {}
    for fid, iri in entities:
        if iri.startswith(str(SEOVOC)):
            if iri in anchored:
                continue
            anchored.add(iri)
            wanted = iri[len(SEOVOC):]
        elif fid in local_names:
            # An external term holding a seovoc local name, e.g. schema:WebPage.
            wanted = re.sub(r"\W+", "-", iri.split("//", 1)[1]).strip("-")
        else:
            continue
        if wanted != fid:
            mapping[fid] = wanted
    if mapping:
        pattern = re.compile(r'(id="|href="#)(' + "|".join(map(re.escape, mapping)) + r')"')
        html = pattern.sub(lambda m: m.group(1) + mapping[m.group(2)] + '"', html)

    # Namespace IRIs without an entry, such as the owl:versionIRI
    # https://w3id.org/seovoc/0.1.0, are linked as in-page fragments; link
    # them to the IRI instead.
    ids = set(re.findall(r'id="([^"]+)"', html))
    return re.sub(
        r'href="#([^"]+)"',
        lambda m: m.group(0) if m.group(1) in ids else f'href="{SEOVOC}{m.group(1)}"',
        html,
    )


def build_reference_html(g: Graph, dest: Path, site_url: str):
    from pylode import OntPub

    # pyLODE cannot split a namespace IRI ending in "/" without a declared
    # preferred namespace, so supply one on a copy of the graph.
    doc_graph = Graph()
    for t in g:
        doc_graph.add(t)
    doc_graph.add((ONTOLOGY, VANN.preferredNamespacePrefix, Literal("seovoc")))
    doc_graph.add((ONTOLOGY, VANN.preferredNamespaceUri, Literal(str(SEOVOC))))

    html = fix_anchors(OntPub(ontology=doc_graph).make_html())
    banner = (
        '<div style="padding:.6em 1em;background:#f4f4f8;border-bottom:1px solid #ddd;'
        'font-family:sans-serif;font-size:.9em">'
        f'<a href="{site_url}">SEOntology guide</a> · '
        f'<a href="{site_url}reference/index.md">Markdown term index</a> · '
        f'<a href="{site_url}seovoc.ttl">Turtle</a> · '
        f'<a href="{site_url}seovoc.owl">RDF/XML</a> · '
        f'<a href="{site_url}seovoc.jsonld">JSON-LD</a>'
        "</div>"
    )
    alternates = (
        f'<link rel="alternate" type="text/turtle" href="{site_url}seovoc.ttl">'
        f'<link rel="alternate" type="application/rdf+xml" href="{site_url}seovoc.owl">'
        f'<link rel="alternate" type="application/ld+json" href="{site_url}seovoc.jsonld">'
        f'<link rel="alternate" type="text/markdown" href="{site_url}reference/index.md">'
    )
    html = html.replace("</head>", alternates + "</head>", 1)
    html = re.sub(r"(<body[^>]*>)", r"\1" + banner, html, count=1)
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "index.html").write_text(html, encoding="utf-8")


def build_llms_txt(config, version: str) -> str:
    site_url = config["site_url"]
    lines = [
        "# SEOntology",
        "",
        "> SEOntology (namespace https://w3id.org/seovoc/, prefix seovoc:) is a "
        "Schema.org-aligned OWL 2 ontology for modeling SEO workflows — pages, queries, "
        "links, content chunks, search and analytics metrics, quality scores and "
        "structured-data profiles — as provenance-aware knowledge graphs.",
        "",
        f"Current version: {version}. Every page below is also available as Markdown; "
        "the links point to those Markdown files.",
        "",
        "## Ontology",
        "",
        f"- [Term index]({site_url}reference/index.md): every class and property with description, domain and range",
        f"- [Turtle]({site_url}seovoc.ttl): the ontology in text/turtle",
        f"- [JSON-LD]({site_url}seovoc.jsonld): the ontology in application/ld+json",
        f"- [JSON-LD context]({site_url}context.jsonld): use as \"@context\" to write SEOntology data with short term names",
        f"- [RDF/XML]({site_url}seovoc.owl): the ontology in application/rdf+xml",
        "",
        "## Guide",
        "",
    ]
    for url, page in _rendered_pages():
        line = f"- [{page['title']}]({site_url}{url}index.md)"
        if page.get("description"):
            line += f": {page['description']}"
        lines.append(line)
    lines += [
        "",
        "## Optional",
        "",
        f"- [Full content]({site_url}llms-full.txt): the guide and term index in one file",
        f"- [Source repository]({REPO_URL})",
        "",
    ]
    return "\n".join(lines)


def on_files(files, config):
    # Images shared with the README live in .assets/, outside docs_dir.
    for name in ("seontology_logo.png", "seontology-doodle.png"):
        files.append(File.generated(config, f"assets/images/{name}", abs_src_path=str(ROOT / ".assets" / name)))
    return files


def on_nav(nav, config, files):
    # List pages in llms.txt in navigation order rather than build order.
    _pages.clear()
    for page in nav.pages:
        _pages[page.url] = None
    return nav


def on_page_markdown(markdown, page, config, files):
    # Repository-relative links to examples/ point outside docs_dir; send
    # them to the copies published with the site.
    markdown = re.sub(r"\]\((?:\.\./)+examples/", "](" + config["site_url"] + "examples/", markdown)
    _pages[page.url] = {
        "title": page.title,
        "description": page.meta.get("description"),
        "markdown": markdown,
    }
    return markdown


def on_post_build(config):
    site_dir = Path(config["site_dir"])
    site_url = config["site_url"]
    g = load_ontology()
    version = ontology_version(g)

    for name in ("seovoc.ttl", "seovoc.owl"):
        shutil.copy2(ROOT / name, site_dir / name)
    (site_dir / "seovoc.jsonld").write_text(
        g.serialize(format="json-ld", context=build_context(g)["@context"], indent=2),
        encoding="utf-8",
    )
    (site_dir / "context.jsonld").write_text(
        json.dumps(build_context(g), indent=2) + "\n", encoding="utf-8"
    )
    shutil.copytree(ROOT / "examples", site_dir / "examples", dirs_exist_ok=True)

    build_reference_html(g, site_dir / "reference", site_url)
    reference_md = reference_markdown(g, version, site_url)
    (site_dir / "reference" / "index.md").write_text(reference_md, encoding="utf-8")

    for url, page in _rendered_pages():
        out = site_dir / url / "index.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page["markdown"], encoding="utf-8")

    (site_dir / "llms.txt").write_text(build_llms_txt(config, version), encoding="utf-8")
    full = [f"# SEOntology — full content (version {version})", ""]
    for url, page in _rendered_pages():
        full += [f"<!-- source: {site_url}{url} -->", page["markdown"].strip(), ""]
    full += [reference_md]
    (site_dir / "llms-full.txt").write_text("\n".join(full), encoding="utf-8")

    log.info("SEOntology %s: reference, artifacts and llms.txt written", version)
