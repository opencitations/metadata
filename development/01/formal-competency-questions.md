# formal competency questions 1

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

## CQ1.1. Bibliographic references and in-text reference pointers

Given a paper X, list (1) all the cited bibliographic references, and (2) their related in-text reference pointers.

```
SELECT distinct ?plLit ?pl ?rpLit ?rp ?beLit
WHERE {
  <https://w3id.org/oc/br/0701> frbr:part ?be.
  ?be a biro:BibliographicReference ; c4o:hasContent ?beLit .
  ?rp c4o:denotes ?be .
  OPTIONAL {?rp c4o:hasContent ?rpLit. }
  OPTIONAL {?pl co:element ?rp ; c4o:hasContent ?plLit. }
}
ORDER BY ?plLit ?rpLit

```

## CQ1.2. Counting of in-text reference pointers

Return bibliographic references and the number of times it is cited in a publication (i.e. the number of in-text reference pointers that denote the same bibliographic reference).

```
SELECT (COUNT(distinct ?rp) as ?count) ?beLit
WHERE {
  <https://w3id.org/oc/br/0701> frbr:part ?be.
  ?be a biro:BibliographicReference ; c4o:hasContent ?beLit .
  ?rp c4o:denotes ?be .
}
GROUP BY ?beLit
ORDER BY DESC(?count)
```

## CQ1.3. In-text reference pointers in lists

Return in-text reference pointers that co-occur within in the same list of in-text reference pointers.

```
SELECT ?rp ?list
WHERE { ?rp a c4o:InTextReferencePointer ;
  ^co:element ?list .
    }
```

# CQ1.4. Order of pointers in lists of pointers

List the next in-text reference pointer in a list of in-text reference pointers.

```
SELECT ?nextRp
WHERE { ?rp a c4o:InTextReferencePointer ; oco:hasNext ?nextRp .
  ^co:element ?list .
    }
```

# CQ1.5. Identifiers of reference pointers

Return the XPath identifying an in-text reference pointer in the source XML document.

```
SELECT ?xpath
WHERE { ?rp a c4o:InTextReferencePointer ; datacite:hasIdentifier ?id .
  ?id literal:hasLiteralValue ?xpath ; datacite:usesIdentifierScheme datacite:xpath .
    }
```
