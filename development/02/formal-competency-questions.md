# formal competency questions 2

Prefixes

```
prefix biro: <http://purl.org/spar/biro/>
prefix co: <http://purl.org/co/>
prefix c4o: <http://purl.org/spar/c4o/>
prefix cito: <http://purl.org/spar/cito/>
prefix datacite: <http://purl.org/spar/datacite/>
prefix dcterms: <http://purl.org/dc/terms/>
prefix deo: <http://purl.org/spar/deo/>
prefix doco: <http://purl.org/spar/doco/>
prefix fabio: <http://purl.org/spar/fabio/>
prefix frbr: <http://purl.org/vocab/frbr/core#>
prefix literal: <http://www.essepuntato.it/2010/06/literalreification/>
prefix oa: <http://www.w3.org/ns/oa#>
prefix oco: <https://w3id.org/oc/ontology/>
prefix pro: <http://purl.org/spar/pro/>
prefix prov: <http://www.w3.org/ns/prov#>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix xsd: <http://www.w3.org/2001/XMLSchema#>
```

## CQ2.1. Document components in which pointers occur

Given a document X, for each reference, retrieve all the document components (section/paragraph/sentence/text chunk) wherein in-text reference pointers are located.

```
SELECT DISTINCT ?rp ?sent (group_concat(distinct ?des; separator="; ") as ?parents) ?beLit
WHERE {
  <https://w3id.org/oc/ccc/br/0701> frbr:part ?be.
  ?be a biro:BibliographicReference ; c4o:hasContent ?beLit .
  ?rp c4o:denotes ?be .

  {?rp ^c4o:isContextOf ?sent . ?des frbr:part+ ?sent .} UNION {?rp ^co:element? / ^c4o:isContextOf ?sent . ?des frbr:part+ ?sent .}
}
GROUP BY ?rp ?sent ?parents ?beLit
ORDER BY ?beLit
```

## CQ2.2. Bibliographic references co-cited in the same document component

List all the bibliographic references in the document X that are cited within a particular document component (e.g. sentence or text chunk).

```
SELECT DISTINCT ?rp ?sent (group_concat(distinct ?des; separator="; ") as ?parents) ?beLit
WHERE {
  <https://w3id.org/oc/ccc/br/0701> frbr:part ?be.
  ?be a biro:BibliographicReference ; c4o:hasContent ?beLit .
  ?rp c4o:denotes ?be .

  {?rp ^c4o:isContextOf ?sent . ?des frbr:part+ ?sent .} UNION {?rp ^co:element? / ^c4o:isContextOf ?sent . ?des frbr:part+ ?sent .}
}
GROUP BY ?sent ?rp ?parents ?beLit
ORDER BY ?beLit
```
