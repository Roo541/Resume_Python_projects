import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import math

import Agents_Stocks

initial = 10000
bank_account= initial
stocks = 0
amount = 0

style.use('ggplot')

start = dt.datetime(2018,01,01)
end = dt.datetime(2018,11,02)
ticker = 'INTC'

df = web.DataReader(ticker, 'yahoo', start, end)


df['9MA'] = df['Adj Close'].rolling(window = 9, min_periods = 0).mean() 
df['50MA'] = df['Adj Close'].rolling(window = 50, min_periods = 0).mean()
print df.index[0]		
net = np.zeros((len(df['Adj Close'])))			
net[10] = Agents_Stocks.bank_account[0]+ Agents_Stocks.amount*df['Adj Close'][1]			
print net
a, b , net, t  = Agents_Stocks.Market(Agents_Stocks.bank_account, Agents_Stocks.stocks, df, Agents_Stocks.amount)

e = float((Net[t]/initial)-1)*100

print 'Bank Account %d' %a,'\n', 'Stocks of', ticker, 'held %d' %b, '\n', 'Net worth %d' %Net[t], '\n', 'Return Percentage %f' %e, '%'

g = np.arange(0, len(Net), 1)

plt.figure()
plt.plot(df.index, Net, label = 'Net Worth')
plt.legend()

plt.figure()
ax1 = plt.subplot2grid((6,1),(0,0), rowspan = 5 , colspan = 1 )
ax2 = plt.subplot2grid((6,1),(5,0), rowspan = 5, colspan = 1, sharex = ax1)


ax1.plot(df.index, df['Adj Close'], label = 'price')
ax1.plot(df.index, df['9MA'], label = '9MA')
ax1.plot(df.index, df['50MA'], label = '50MA')
ax2.bar(df.index, df['Volume'], label = 'Volume')
ax1.legend()
ax2.legend()
plt.show()
