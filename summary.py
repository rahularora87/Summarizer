
#! usr/bin/env python3
# John Bennett
# Nov 14, 2016

import re
import nltk
import string
import os
import nltk.tokenize
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer


stemmer = PorterStemmer()
def wordStemmer(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def wordFrequency(words):
    fdist = FreqDist(words)
    fdist = fdist.most_common(50)
    return fdist

def textProcess(file):
    file = open(file, 'r')
    raw = file.read()
    raw = raw.lower()
    wordTokens = nltk.word_tokenize(raw)
    file.close()
    return wordTokens

def textCleanup(tokens):
    stopWords = set(stopwords.words('english'))
    newWordList = [w for w in tokens if not w in stopWords]
    newWordList = [i for i in newWordList if not i in string.punctuation]
    return newWordList
    
def main():       
    exp = textProcess('sample.txt')
    exp = textCleanup(exp)
    exp = wordStemmer(exp, stemmer)
    exp = wordFrequency(exp)
    print(exp)
    
    
if __name__ == '__main__':
    main()

