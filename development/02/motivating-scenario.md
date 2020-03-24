# motivating scenario 2

## Name
In-text references in context

## Description

Identify and retrieve the structural elements wherein in-text reference pointers appear (e.g. the sentence, the paragraph, the section), their titles, and their hierarchy. Discover in-text reference pointers that co-occur in the same element.

## Example

Consider the following article:

```
Piwowar H, Priem J, Larivière V, Alperin JP, Matthias L, Norlander B, Farley A, West J, Haustein S. 2018. The state of OA: a large-scale analysis of the prevalence and impact of Open Access articles. PeerJ 6:e4375 doi:10.7717/peerj.4375
```

Consider the following in-text references that appear in the full-text of the article:

```
Section “Introduction”
“Third, Sci-Hub (a website offering pirate access to full text articles) has built an enormous user base, provoking newly intense conversation around the ethics and efficiency of paywall publishing (Bohannon, 2016; Greshake, 2017).”

Section “Methods”
“At the time of writing, oaDOI processes approximately 500,000 requests daily–roughly twice the daily uses of Sci-Hub (Bohannon, 2016).”
```

The in-text references denote the following bibliographic references, hereon called paper Y and paper Z

```
[paper Y] Bohannon J. 2016. Who’s downloading pirated papers? Everyone. Science 352(6285):508-512

[paper Z] Greshake B. 2017. Looking into Pandora’s Box: the content of Sci-Hub and its usage [version 1; referees: 2 approved, 2 approved with reservations] F1000Research 6 Article 541
```

 * Paper X cites paper Y and paper Z.
 * Paper Y is cited twice: in section “Introduction”, paragraph 1, sentence 6; in section “Methods”, paragraph 4, sentence 26.
 * Paper Z is cited only once: in section “Introduction”, paragraph 1, sentence 6
 * Paper Y and Paper Z co-occur in the same list of in-text reference pointers in  section “Introduction”, paragraph 1, sentence 6.
