#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint , os , json, csv
from lxml import etree as ET
from collections import defaultdict , OrderedDict
from requests import get
from bs4 import BeautifulSoup
from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag

pp = pprint.PrettyPrinter(indent=2)

# Identifying keywords/terms
def extract_data_terms(path_data,path_xml_terms):
    """takes a folder of jats/xml files in input
    and returns a json of definitions of xml elements and attributes ordered by frequency"""
    element_set = defaultdict(set)
    count_elem , count_elem_attr = list(), list()
    for xml_doc in os.listdir(path_data):
        try:
            filename = os.fsdecode(xml_doc)
            xml_doc = os.path.join(path_data, filename)
            xmlp = ET.XMLParser(encoding="utf-8")
            tree = ET.parse(xml_doc, xmlp)
            root = tree.getroot()
            for elem in root.iter():
                count_elem.append(elem.tag)
                for attr in elem.attrib:
                    count_elem_attr.append((elem.tag, attr))
                    element_set[elem.tag].add(attr)
        except:
            print("ERROR",filename)
            continue
    # sort by frequency
    statistics_json = defaultdict(dict)
    for k,v in element_set.items():
        for attr in v:
            statistics_json[k]['count'] = count_elem.count(k)
            statistics_json[k][attr] = count_elem_attr.count((k,attr))
    statistics_json = OrderedDict(sorted(statistics_json.items(), key=lambda i: i[1]['count'], reverse=True))
    print("XML terms extracted")

    # expand definitions
    expanded_json = {}
    for i,(k, v) in enumerate(statistics_json.items()):
        url = 'https://jats.nlm.nih.gov/publishing/tag-library/1.2/element/'+k+'.html'
        try:
            response = get(url)
            html_soup = BeautifulSoup(response.text, 'html.parser')
            definition = html_soup.find('h1', class_ = 'elementname').text

            # clean definitions
            definition = definition.replace('\n','')
            if definition is not None:
                expanded_json[definition] = v
            else:
                expanded_json[k] = v
        except:
            expanded_json[k] = v
    print("XML terms definitions added")

    with open(path_xml_terms, 'w') as labels_file:
        json.dump(expanded_json, labels_file, indent=4)
    print("xml terms created at:",path_xml_terms)
    return path_xml_terms

# extract terms from oco
def extract_ontology_terms(xml_doc,path_onto_terms):
    labels = []
    # filename = os.fsdecode(xml_doc)
    # xml_doc = os.path.join(filename)
    xmlp = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(xml_doc, xmlp)
    root = tree.getroot()
    rdf = {'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}
    for elem in root.findall("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description"):
        definition = elem.findall("{http://www.w3.org/2000/01/rdf-schema#}label")[0].text \
            if len(elem.findall("{http://www.w3.org/2000/01/rdf-schema#}label")) != 0 else None
        name = elem.xpath("@rdf:about", namespaces=rdf)[0].rsplit('/', 1)[1] \
            if elem.xpath("@rdf:about", namespaces=rdf)[0] is not None else None
        if definition is not None:
            labels.append(definition)
        else:
            labels.append(name)
    print("ontology terms extracted",labels)

    with open(path_onto_terms, 'w') as labels_file:
        for label in labels:
            labels_file.write('%s\n' % label)
    print("ontology terms created at",path_onto_terms)
    return path_onto_terms


# source: https://nlpforhackers.io/wordnet-sentence-similarity/
def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'
    elif tag.startswith('V'):
        return 'v'
    elif tag.startswith('J'):
        return 'a'
    elif tag.startswith('R'):
        return 'r'
    else:
        return None

def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
    try:
        syn = wn.synsets(word.lower(),wn_tag)[0]
        return syn
    except:
        return None

def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence1 = [(w,penn_to_wn(t)) if penn_to_wn(t) is not None else None for (w,t) in sentence1]
    sentence2 = pos_tag(word_tokenize(sentence2))
    sentence2 = [(w,penn_to_wn(t)) if penn_to_wn(t) is not None else None for (w,t) in sentence2]
    sentence1 = [ss for ss in sentence1 if ss]
    sentence2 = [ss for ss in sentence2 if ss]
    # sentence1 = word_tokenize(sentence1)
    # sentence2 = word_tokenize(sentence2)

    # Get the synsets for the tagged words
    # synsets1 = [tagged_to_synset(tagged_word, tag) for (tagged_word,tag) in sentence1]
    # synsets2 = [tagged_to_synset(tagged_word, tag) for (tagged_word,tag) in sentence2]
    synsets1 = [wn.synsets(word.lower(),t)[0] if len(wn.synsets(word.lower(),t)) != 0 else None for word,t in sentence1]
    synsets2 = [wn.synsets(word.lower(),t)[0] if len(wn.synsets(word.lower(),t)) != 0 else None for word,t in sentence2]
    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
    score, count = 0.0, 0

    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        s = [synset.path_similarity(ss) for ss in synsets2]
        s = [ss for ss in s if ss]
        best_score = max(s) if len(s) !=0 else None

        # Check that the similarity could have been computed
        if best_score is not None:
            score += best_score
            count += 1

    # Average the values
    if count > 0:
        score /= count
    else:
        score = 0
    return score

def symmetric_sentence_similarity(sentence1, sentence2):
    """ compute the symmetric sentence similarity using Wordnet """
    return (sentence_similarity(sentence1, sentence2) + sentence_similarity(sentence2, sentence1)) / 2
