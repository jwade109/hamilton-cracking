#!/usr/bin/env bash

from fuzzysearch import find_near_matches
from fuzzywuzzy import process
import numpad
import re
from random import randrange

words = re.split('\s|\n|-', open("lyrics.txt", encoding="utf8").read())
while "" in words:
    words.remove("")
for i, word in enumerate(words):
    words[i] = re.sub(r'\W+', '', word.lower())

first_letters = ""
for word in words:
    first_letters += word[0];

def fuzzy_extract(qs, ls, threshold, distance):
    '''fuzzy matches 'qs' in 'ls' and returns list of
    tuples of (word,index)
    '''
    for word, _ in process.extractBests(qs, (ls,), score_cutoff=threshold):
        for match in find_near_matches(qs, word, max_l_dist=distance):
            match = word[match.start:match.end]
            index = ls.find(match)
            yield (match, index)

numpad_input = [7, 6, 6, 8, 0, 0]
max_distance = 0

for i in range(2, 10):
    for j in range(2, 10):
        numpad_input[4] = i
        numpad_input[5] = j

        print("Computing for password: " + str(numpad_input))
        query_strings = numpad.get_possible_passwords(numpad_input)
        past_matches = []

        print("{:20}{:20}{}".format("QUERY", "MATCH", "LYRICS"))
        for query_string in query_strings:
            for distance in range(0, max_distance + 1):
                results = fuzzy_extract(query_string, first_letters, 0, distance)
                for match, index in results:
                    if match not in past_matches:
                        # past_matches.append(match)
                        print("{:20}{:20}{}".format(query_string, match,
                            " ".join(words[index:index+len(match)+5])))
