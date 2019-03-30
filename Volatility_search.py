import numpy as np
import matplotlib.pyplot as plt
import math
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style
import csv
import time

plt.style.use('ggplot')

start = dt.datetime(2018, 12, 01)
end = dt.datetime(2019, 03, 29)

ticker = ['AAPL']*495
t = 0 

with open('s&p500_list.csv') as my_file:
	csv_reader = csv.reader(my_file, delimiter = ',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			ticker[t] = row[0]
			t = t + 1
period = 21
high_vol = []
low_vol = []
for i in range(1,len(ticker)):
	print i, ticker[i]
	df = web.DataReader(ticker[i], 'yahoo', start, end)
	df['Vol'] = df['Adj Close'].pct_change(periods = 21)
	df['Vol'] = df['Vol']*100	
	recent = df['Vol'][-1:].mean()
	# ~ print df['Vol'][-period:]
	# ~ print recent
	if abs(recent) < 1:
		low_vol.append(ticker[i])
		low_vol.append(recent)
		print i, ticker[i], recent
	if abs(recent) > 10:
		high_vol.append(ticker[i])
		high_vol.append(recent)
		print i, ticker[i], recent
		
print '\n High Volatility stocks, total count is:', len(high_vol)
for i in range(len(high_vol)):
	if i+1 < len(high_vol) and i%2 == 0:
		print high_vol[i], high_vol[i+1]

print '\n Low Volatility stocks, total count is:', len(low_vol)
for i in range(len(low_vol)):
	if i+1 < len(low_vol) and i%2 == 0:
		print low_vol[i], low_vol[i+1]

