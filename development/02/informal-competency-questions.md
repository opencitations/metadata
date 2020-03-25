# informal competency questions 2

## CQ2.1. Document components in which pointers occur

Given a document X, for each reference, what are all the document components (section/paragraph/sentence/text chunk) wherein in-text reference pointers are located.

*Outcome*

A list of pairs of in-text reference pointers and the XPath of the element containing them.

*Example*

"Bohannon, 2016", "/article/sec[1]/p[1]"
"Greshake, 2017", "/article/sec[1]/p[1]"
"Bohannon, 2016", "/article/sec[3]/p[4]"


## CQ2.2. In-text reference pointers co-cited in the same document component

What are all the in-text reference pointers in the document X that are cited in the same document component (e.g. paragraph).

*Outcome*

A list of pairs of in-text reference pointers and the XPath of the element containing them.

*Example*

"/article/sec[1]/p[1]", "Bohannon, 2016", "Greshake, 2017"
"/article/sec[3]/p[4]", "Bohannon, 2016"
