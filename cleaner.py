import HTMLParser
import pandas as pd
import re
from bs4 import BeautifulSoup



print("normalization begins")
htmlparser = HTMLParser.HTMLParser()
df = pd.read_csv("tweets_data.csv", delimiter = ",", encoding="utf-8")
df['tweet']=df['tweet'].str.encode('utf-8')
df['tweet'] = htmlparser.unescape(df['tweet'])
df=df.dropna()
df = df.replace(r'\\n',' ', regex=True)
df.replace({ r'\A\s+|\s+\Z': '', '\n' : ' '}, regex=True, inplace=True)
df['tweet'] = df['tweet'].replace(r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True)
df["tweet"] = df['tweet'].str.replace('[^\w\s]','')
print("normalization ends")

df.to_csv('normalize.csv')
print("normalized data")

