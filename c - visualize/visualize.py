#!/usr/bin/env python
# encoding: utf-8

import pandas as pd 
import matplotlib.pyplot as plt

# read csv 1nto a data frame 
sentiment = pd.read_csv("Patriots_sentiment.csv")

# graph data
sentiment.plot()

plt.title('@Patriots twitter sentiment during superbowl')

plt.ylabel('sentiment')
plt.xlabel('time')


x = range(0)
y = range(0)
plt.xticks(x," ")

plt.legend(bbox_to_anchor=(1.00, 0.00))



plt.show()


#sentiment['sentiment'] = (sentiment['sentiment'] !='n').astype(int)
#print sentiment.head()
