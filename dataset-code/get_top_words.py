import matplotlib.pyplot as plt
import plotly.plotly as py
from load_jsons import *
import operator

print "Loading data"
with open("../../datasets/instaBarcelona/captions.json","r") as file:
    data = json.load(file)

symbols = ['.','/','\\',',']
stop = ['que','the','and','para','con','los','por','una','del','las','for','you','with','this','mas','are','como','that']

print "Counting words"
words = {}
for k,v in data.iteritems():
    caption = v.replace('#', ' ')
    caption = caption.lower()
    c_words = caption.split()

    # Filter stop_words
    filtered_words = []
    for i in c_words:
        if i not in stop: filtered_words.append(i)
    print len(filtered_words)

    for w in filtered_words:

        # Filter short words
        if len(w) < 3: continue

        # Filter symbols
        symbol = False
        for s in symbols:
            if s in w:
                symbol = True
                break
        if symbol: continue


        if w not in words:
            words[w] = 1
        else:
            words[w] = words[w] + 1

print "Number of words: " + str(len(words))
print "Word with max repetitions has:  " + str(max(words.values()))


words_sorted = sorted(words.items(), key=operator.itemgetter(1))

#Print top words
num2print = 50
for i in range(num2print):
    print words_sorted[-i-1][0]


#Plot
words_count_sorted = words.values()
words_count_sorted.sort(reverse=True)
topX = 20
x = range(topX-1)
my_xticks = []
for l in range(1,topX):
    my_xticks.append(words_sorted[-l-1][0])
plt.xticks(x, my_xticks, rotation=90, size=8)
width = 1/1.5
plt.bar(x, words_count_sorted[1:topX], width, color="blue")
plt.title("Num of top words")
plt.show()

print "Done"