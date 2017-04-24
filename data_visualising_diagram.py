import pandas
import json

import vincent

from counting_words import preprocess

"""
dates_ITAvWAL = []
# f is the file pointer to the JSON data set
f ='stream_president.json'
for line in f:
    tweet = json.loads(line)
    # let's focus on hashtags only at the moment
    terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]
    # track when the hashtag is mentioned
    if '#itavwal' in terms_hash:
        dates_ITAvWAL.append(tweet['created_at'])

# a list of "1" to count the hashtags
ones = [1] * len(dates_ITAvWAL)
# the index of the series
idx = pandas.DatetimeIndex(dates_ITAvWAL)
# the actual series (at series of 1s for the moment)
ITAvWAL = pandas.Series(ones, index=idx)

# Resampling / bucketing
per_minute = ITAvWAL.resample('1Min', how='sum').fillna(0)

time_chart = vincent.Line(ITAvWAL)
time_chart.axis_titles(x='Time', y='Freq')
time_chart.to_json('president_term_time_diagram.json')


"""


dates_ELECTION = []
# f is the file pointer to the JSON data
f = 'stream_president.json'
with open(f, 'r') as file:
    for line in file:
        tweet = json.loads(line)
        if 'text' in tweet.keys() and 'created_at' in tweet.keys():
            terms_hash = [term for term in preprocess(tweet['text']) if not term.startswith('#') and not term.startswith('@')]
            print(terms_hash)
            is_there = False
            for hashword in terms_hash:
                if "president" in hashword:
                    is_there = True
            if is_there:
                print("DID")
                print(tweet['created_at'])
                dates_ELECTION.append(tweet['created_at'])

# a list of "1" to count the hashtags
print("len(dates_ELECTION)")
print(len(dates_ELECTION))
ones = [1] * len(dates_ELECTION)
print("ONES")
print(ones)
# the index of the series
idx = pandas.DatetimeIndex(dates_ELECTION)
print("INDEX")
print(idx)
print(idx[0])

ELECTION = pandas.Series(ones, index=idx)
print("ELECTION")
print(ELECTION)
# Resampling / bucketing
per_sec = ELECTION.resample("AS").sum().fillna(0) // "3 S"
print("per_sec")
for it in per_sec:
    if it == "nan":
        print("aha")
time_chart = vincent.Line(per_sec)
print("time_chart")
print(time_chart)
time_chart.axis_titles(x='Time', y='Freq')
print(time_chart)
time_chart.to_json('president_time_freq_diagram.json')