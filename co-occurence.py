import json
import operator
import string
from collections import defaultdict

from nltk.corpus import stopwords

from tokenization import preprocess

# remember to include the other import from the previous post

com = defaultdict(lambda: defaultdict(int))
lst_of_data = []

punctuation = list(string.punctuation)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
stop = stopwords.words('english') + punctuation + ['rt', 'RT', 'via' '!', '`']  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

with open('stream_president.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        print(tweet)
        lst_of_data.append((tweet))
        if (tweet['text']):
            terms_only = [term for term in preprocess(tweet['text']) if term not in stop and not term.startswith(('@'))]
                      #if #term not in stop and

        # Build co-occurrence matrix
        for i in range(len(terms_only) - 1):
            for j in range(i + 1, len(terms_only)):
                w1, w2 = sorted([terms_only[i], terms_only[j]])
                if w1 != w2:
                    com[w1][w2] += 1

"""
print("\n")
print(lst_of_data)
data = open("locations.txt", "w")
for i in lst_of_data:
    data.write(str(i));
    data.write("\n")
"""

com_max = []
# For each term, look for the most common co-occurrent terms
for t1 in com:
    t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
print(terms_max[:5])