import csv
import pandas as pd
import numpy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    return snt

print("Sentimental analysis begins")

with open('normalize.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    compounds = []
    emotions = []
    temp = []
    sum = 0.0
    for row in readCSV:
	sentiment_value = print_sentiment_scores(row[4])
	compounds.append(sentiment_value["compound"])
    for compound in compounds:
	dummy = 0.0
	compound = dummy + compound
	sum += compound
	if compound > 0.0:
		emotion = 'positive'
    	elif compound < 0.0:
		emotion = 'negative'
    	else:
		emotion = 'neutral'
    	emotions.append(emotion)


print("Sentimenatl analysis ends")

#transformation of extracted data using pandas

df = pd.read_csv("normalize.csv")
df['sentiment_score'] =  pd.Series(compounds)
df['sentiment'] = pd.Series(emotions)
df.to_csv('senti.csv')

df.drop(['id', 'user', 'created_at'], axis=1, inplace=True)
df.to_csv('processed.csv')

print("saved sentimental analysis")
