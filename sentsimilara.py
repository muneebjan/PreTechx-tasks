# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:09:35 2018

@author: aa
"""
from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag

def sentence_similarity(sentence1, sentence2):

    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
 
    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
 
    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
 
    score, count = 0.0, 0
 
    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        best_score = max([synset.path_similarity(ss) for ss in synsets2])
 
        # Check that the similarity could have been computed
        if best_score is not None:
            score += best_score
            count += 1
 
    # Average the values
    score /= count
    return score
 
sentences = [
    "Let us meet at cofe shop",
    "Reehan and ali meet at pizza shop",
    "Cats are beautiful",
    "They will meet at burger point",
]
 
focus_sentence = "Let us meet at cofe shop"
 
for sentence in sentences:
    print "Similarity(\"%s\", \"%s\") = %s" % (focus_sentence, sentence, sentence_similarity(focus_sentence, sentence))
     
    