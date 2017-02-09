#!/usr/bin/env python
# encoding: utf-8

import pandas as pd 
from textblob import TextBlob

# read csv 1nto a data frame 
tweets = pd.read_csv("Patriots_tweets.csv")

# clean the data 
tweets = tweets.drop('id', 1)

# sentiment analysis
for i in tweets.iterrows():
	text = TextBlob(str(i[1]))
	if(text.sentiment.polarity):
		print text.sentiment.polarity
	else:
		print "."