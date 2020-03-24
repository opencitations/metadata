# motivating scenario 1

## Name
In-text references and lists of in-text references

## Description

Basic operations on in-text references, like retrieve all the in-text reference pointers, retrieve all related bibliographic references, identify whether reference pointers appear in lists or alone, and count the number of times a bibliographic reference is cited in the text (i.e. the number of reference pointers).

Pointers and lists can be identified with respect to the XML document by means of a XPath selector.

## Example

Consider the following article:

```
Piwowar H, Priem J, Larivière V, Alperin JP, Matthias L, Norlander B, Farley A, West J, Haustein S. 2018. The state of OA: a large-scale analysis of the prevalence and impact of Open Access articles. PeerJ 6:e4375 doi:10.7717/peerj.4375
```

Consider the following in-text references that appear in the full-text of the article:

```
(Bohannon, 2016; Greshake, 2017)
(Bohannon, 2016)
```

The in-text references denote the following bibliographic references, hereon called paper Y and paper Z

```
[paper Y] Bohannon J. 2016. Who’s downloading pirated papers? Everyone. Science 352(6285):508-512

[paper Z] Greshake B. 2017. Looking into Pandora’s Box: the content of Sci-Hub and its usage [version 1; referees: 2 approved, 2 approved with reservations] F1000Research 6 Article 541
```

 * Paper X cites paper Y and paper Z.
 * Paper Y is cited twice.
 * Paper Z is cited only once.
 * Paper Y and Paper Z co-occur in the same list of in-text reference pointers.
