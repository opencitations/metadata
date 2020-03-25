# informal competency questions 1

## CQ1.1. Bibliographic references and in-text reference pointers

Given a paper X, what are all the cited bibliographic references, and their related in-text reference pointers.

*Outcome*

A list of pairs of bibliographic references and in-text reference pointers.

*Example*

"Bohannon J. 2016. Who’s downloading pirated papers? Everyone. Science 352(6285):508-512", "Bohannon, 2016"
"Bohannon J. 2016. Who’s downloading pirated papers? Everyone. Science 352(6285):508-512", "Bohannon, 2016"
"Greshake B. 2017. Looking into Pandora’s Box: the content of Sci-Hub and its usage [version 1; referees: 2 approved, 2 approved with reservations] F1000Research 6 Article 541", "Greshake, 2017"

## CQ1.2. Counting of in-text reference pointers

Given a paper X, what are the bibliographic references and the number of times they are cited in (i.e. the number of in-text reference pointers that denote the same bibliographic reference).

*Outcome*

A list of pairs of bibliographic references and an integer.

*Example*

"Bohannon J. 2016. Who’s downloading pirated papers? Everyone. Science 352(6285):508-512", 2
"Greshake B. 2017. Looking into Pandora’s Box: the content of Sci-Hub and its usage [version 1; referees: 2 approved, 2 approved with reservations] F1000Research 6 Article 541", 1

## CQ1.3. In-text reference pointers in lists

What are the in-text reference pointers that co-occur in a list.

*Outcome*

A list of pairs of lists and in-text reference pointers.

*Example*

"(Bohannon, 2016; Greshake, 2017)","Bohannon, 2016"
"(Bohannon, 2016; Greshake, 2017)","Greshake, 2017"
"(Bohannon, 2016)","Bohannon, 2016"

# CQ1.4. Order of pointers in lists of pointers

Whar are the in-text reference pointers in a list of in-text reference pointers that are followed by another in-text reference pointer.

*Outcome*

A list of pairs of in-text reference pointers.

*Example*

"Bohannon, 2016","Greshake, 2017"

# CQ1.5. Identifiers of reference pointers

What are the XPath identifying in-text reference pointers in the source XML document.

*Outcome*

A list of pairs of in-text reference pointers and XPath strings.

*Example*

"Bohannon, 2016", "/article/sec[1]/p[1]/xref[1]"
"Greshake, 2017", "/article/sec[1]/p[1]/xref[2]"
"Bohannon, 2016", "/article/sec[3]/p[4]/xref[1]"
