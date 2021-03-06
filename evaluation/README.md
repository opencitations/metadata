# OCDM evaluation

Includes scripts and data about OCDM evaluation

### `oco_jats_lexical_similarity`

 * `comm_use-A-B-sample` a corpus of around 2800 JATS/XML documents
 * `oco.xml` the OCO ontology
 * `oco_eval.py` utility functions
 * `run.py` the script to extract XML terms, OCO definitions and compute lexical similarity
 * `xml_terms.json` definitions of JATS/XML elements extracted from the
 corpus and expanded with online definitions. Manually flagged with `"include":"True"`
 * `onto_terms.txt` definitions extracted from OCO. Manually flagged with `#` when non-relevant
 * `similarity_data_onto_07.json` results of lexical similarity with a score > 0.7. Manually flagged `"false_positive": "True"`
 * `similarity_data_onto_05.json` results of lexical similarity with a score > 0.5.  Manually flagged `"false_positive": "True"`

### `uptake`

 * views (and unique users) of the [data model webpage](http://opencitations.net/model)
 * `altmetrics.json` [source](https://api.altmetric.com/v1/doi/10.6084/m9.figshare.3443876)

### `vocabulary_coverage`

 * list of evaluated vocabularies and schemas
