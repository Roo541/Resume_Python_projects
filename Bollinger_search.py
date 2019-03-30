import datetime as dt
import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style
import csv

style.use('ggplot')

start = dt.datetime(2018,12,01)
end = dt.datetime(2019,03,26)

ticker = ['a']*495
t = 0
above = []
below = []

order = True
with open('s&p500_list.csv') as my_file:
	csv_reader = csv.reader(my_file, delimiter = ',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			ticker[t] = row[0]
			t = t + 1

for i in range(1,len(ticker)):
	print i, ticker[i]
	df = web.DataReader(ticker[i], 'yahoo', start, end)
	df['20MA'] = df['Adj Close'].rolling(window = 20, min_periods = 0).mean()
	df['20Std'] = df['Adj Close'].rolling(window =20, min_periods = 0).std()
	
	df['UpperBand'] = df['20MA']
	df['LowerBand'] = df['20MA']
	
	for j in range(0,len(df)):
		df['UpperBand'][j] = df['20MA'][j] + df['20Std'][j]*2
		df['LowerBand'][j] = df['20MA'][j] - df['20Std'][j]*2
	
	for t in range(len(df)-5, len(df)):
		if df['Adj Close'][t] <= df['LowerBand'][t]:
			below.append(ticker[i])
			print 'below BBand', ticker[i], below
			break
		if df['Adj Close'][t] >= df['UpperBand'][t]:
			above.append(ticker[i])
			print 'Above BBand', ticker[i], above
			break

	
print '\n Above Bollinger Band tickers are: '
for i in range(len(above)):
	print above[i]

print '\n Below Bollinger Band tickers are: '	
for i in range(len(below)):
	print below[i]
	
