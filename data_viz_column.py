import vincent
import counting_words

word_freq = counting_words.count_terms('stream_president.json')
labels, freq = zip(*word_freq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')
bar.to_json('president_term_freq_column.json')

