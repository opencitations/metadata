#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint , os , json , csv
import oco_eval as oco_eval
from lxml import etree as ET
from collections import defaultdict , OrderedDict
from requests import get
from bs4 import BeautifulSoup
from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag

path_data = 'script/evaluation/oco/comm_use-A-B-sample'
path_onto = 'script/evaluation/oco/oco.xml'
path_xml_terms = 'script/evaluation/oco/xml_terms.json'
path_onto_terms = 'script/evaluation/oco/onto_terms.txt'

xml_terms , ontology_terms = None , None
if os.path.exists(path_xml_terms) is False:
    xml_terms = oco_eval.extract_data_terms(path_data,path_xml_terms)
else:
    with open(path_xml_terms, 'r') as json_file:
        xml_terms = json.loads(json_file.read())

if os.path.exists(path_onto_terms) is False:
    ontology_terms = oco_eval.extract_ontology_terms(path_onto, path_onto_terms)
else:
    ontology_terms = []
    with open(path_onto_terms,'r') as list_file:
        for l in list_file.readlines():
            if l.startswith("# "):
                pass
            else:
                currentPlace = l[:-1]
                ontology_terms.append(currentPlace)

if os.path.exists('script/evaluation/oco/similarity_data_onto_07.json') is False:
    # compute similarity between sentences
    best_matches = defaultdict(dict)
    for xml_term, d in xml_terms.items():
        for onto_term in ontology_terms:
            if "include" in d:
                similarity_score = oco_eval.symmetric_sentence_similarity(xml_term, onto_term)
                if similarity_score > 0.7:
                    best_matches[xml_term][onto_term] = similarity_score
                    best_matches[xml_term]['frequency'] = d["count"]

    with open('script/evaluation/oco/similarity_data_onto_07.json', 'w') as outfile:
        json.dump(best_matches, outfile, indent=4)
    print("output file done!")

if os.path.exists('script/evaluation/oco/similarity_data_onto_05.json') is False:
    # compute similarity between sentences
    best_matches = defaultdict(dict)
    for xml_term, d in xml_terms.items():
        for onto_term in ontology_terms:
            if "include" in d:
                similarity_score = oco_eval.symmetric_sentence_similarity(xml_term, onto_term)
                if similarity_score > 0.5:
                    best_matches[xml_term][onto_term] = similarity_score
                    best_matches[xml_term]['frequency'] = d["count"]

    with open('script/evaluation/oco/similarity_data_onto_05.json', 'w') as outfile:
        json.dump(best_matches, outfile, indent=4)
    print("output file done!")

# xml coverage in oco w 0.5 and w/ 0.7
count_total_xml = 0
for k,v in xml_terms.items():
    if "include" in v:
        count_total_xml += 1

with open('script/evaluation/oco/similarity_data_onto_05.json', 'r') as json_file:
    xml_terms_mapped = json.loads(json_file.read())
    count_xml_mapped_05 = len(xml_terms_mapped)
    count_absent_05 = count_total_xml-count_xml_mapped_05
    count_absent_05_list = []
    for term, d in xml_terms.items():
        if term not in xml_terms_mapped and "include" in d:
            count_absent_05_list.append( (term, d['count']) )

with open('script/evaluation/oco/similarity_data_onto_07.json', 'r') as json_file_07:
    xml_terms_mapped_07 = json.loads(json_file_07.read())
    count_xml_mapped_07 = len(xml_terms_mapped_07)
    count_absent_07 = count_total_xml-count_xml_mapped_07
    count_absent_07_list = []
    for term, d in xml_terms.items():
        if term not in xml_terms_mapped_07 and "include" in d:
            count_absent_07_list.append( (term, d['count']) )
