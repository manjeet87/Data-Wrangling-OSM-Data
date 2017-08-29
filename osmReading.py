#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the
tag name as the key and number of times this tag can be encountered in
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.ElementTree as ET
import pprint

article_file = "example.osm"



def get_tags_itrParse(fname):
    tree = ET.parse(fname)
    tagDict = {}
    for tags in ET.iterparse(fname):
        print (tags)
        if tags[1].tag not in tagDict:
            tagDict[tags[1].tag]=1
            #tags[1].tag.
        else:
            tagDict[tags[1].tag] +=1


    # tagDict[tree._root.tag] = 1
    # root = tree.getroot()
    #
    # for tag in tree.findall('.//'):
    #     if tag.tag not in tagDict:
    #         tagDict[tag.tag]=1
    #     else:
    #         tagDict[tag.tag] +=1

    pprint.pprint(tagDict)

# YOUR CODE HERE

    return tagDict


def mytest():

    data = get_tags_itrParse(article_file)




mytest()