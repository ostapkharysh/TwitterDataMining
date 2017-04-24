import string
from collections import Counter

from pandas import json

from nltk.corpus import stopwords

from tokenization import tokenize, emoticon_re


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


def count_terms(fname):
    punctuation = list(string.punctuation)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    stop = stopwords.words('english') + punctuation + ['rt', 'RT', 'via', '...']  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    with open(fname, 'r') as f:
        count_all = Counter()
        for line in f:
            tweet = json.loads(line)
            # Create a list with all the terms
            if 'text' in tweet.keys():
                terms_all = [term.lower() for term in preprocess(tweet['text']) if term not in stop
                             and not term.startswith(("@", "#")) and len(term) >=3]
                count_all.update(terms_all)
    return count_all.most_common(20)

#print(count_terms('stream_president.json'))
