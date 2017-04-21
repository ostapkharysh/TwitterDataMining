import json
import string
from collections import Counter

import vincent
from nltk.corpus import stopwords

from counting_words import preprocess

punctuation = list(string.punctuation)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
stop = stopwords.words('english') + punctuation + ['rt', 'RT', 'via', '…','’', 'sk']  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
fname = 'stream_president.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_all = [term.lower() for term in preprocess(tweet['text']) if term not in stop
                     and not term.startswith(("@", "#"))]
        # Update the counter
        # print(terms_all)
        #print(terms_all, "\n")
        count_all.update(terms_all)
        # Print the first 5 most frequent words
    print(count_all.most_common(20))
    word_freq = count_all.most_common(20)
    labels, freq = zip(*word_freq)
    data = {'data': freq, 'x': labels}
    bar = vincent.Bar(data, iter_idx='x')
    #bar.to_json('term_freq.json')
    bar.to_json('term_freq.json', html_out=True, html_path='chart.html')
    #python3 - m http.server 888