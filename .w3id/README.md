# w3id redirect rules

`.htaccess` in this directory is the proposed replacement for
[`ids/seovoc/.htaccess`](https://github.com/perma-id/w3id.org/blob/master/ids/seovoc/.htaccess)
in the [perma-id/w3id.org](https://github.com/perma-id/w3id.org) repository, which
controls where `https://w3id.org/seovoc/` and its term IRIs redirect.

Changes from the current rules:

- Browsers (`text/html`) go to the documentation site instead of the GitHub
  repository: the root to the guide, and each term to its entry in the reference
  (`https://w3id.org/seovoc/WebPage` → `.../reference/#WebPage`).
- Turtle and RDF/XML are served from GitHub Pages with proper media types
  instead of `raw.githubusercontent.com`, which serves `text/plain`.
- `application/ld+json` requests get `seovoc.jsonld`.
- `https://w3id.org/seovoc/context.jsonld`, the ontology files and `llms.txt`
  resolve directly.
- The HTML rule runs before the RDF/XML rule, because browsers send
  `application/xml` in their `Accept` header and were matched as RDF/XML.

To apply it, deploy the site first so the targets exist, then open a pull
request against perma-id/w3id.org replacing `ids/seovoc/.htaccess` with this
file. Check the result with:

```bash
curl -sI -H 'Accept: text/html' https://w3id.org/seovoc/WebPage
curl -sI -H 'Accept: text/turtle' https://w3id.org/seovoc/WebPage
curl -sI https://w3id.org/seovoc/context.jsonld
```
