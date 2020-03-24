# formal competency questions 3

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

## CQ 3.1. Citation functions

For each reference pointer retrieve all citation functions associated.

```
SELECT ?rp ?function
WHERE {
        ?rp a c4o:InTextReferencePointer ;
        oco:hasAnnotation ?annotation .
        ?annotation oa:hasBody ?citation .
        ?citation cito:hasCitationCharacterisation ?function .
    }
```
