import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import math

num_agents = 5
num_stocks = 1
bank_account = np.zeros((num_agents))
bank_account[:] = 10000
stocks = np.zeros((num_agents, num_stocks))
stocks[:][:] = 0
amount = 0


def Agent_0(bank_account, stocks, df,t):
	if df['9MA'][t-1] < df['50MA'][t-1] and df['9MA'][t] > df['50MA'][t] and bank_account[0] > df['Adj Close'][t]:
		choice = 'Buy'
		amount = math.floor(bank_account[0]/(df['Adj Close'][t]))
		return choice, amount
	if df['9MA'][t-1] > df['50MA'][t-1] and df['9MA'][t] < df['50MA'][t]: 
		choice = 'Sell'
		amount = stocks
		return choice, amount
	else:
		return 'none', 0

def Agent_1(bank_account, stocks, df, t):
	if df['9MA'][t-1] < df['50MA'][t-1] and df['9MA'][t] > df['50MA'][t] and bank_account[1] > df['Adj Close'][t]:
		choice = 'Buy'
		amount = math.floor(bank_account[1]/(df['Adj Close'][t]))
		return choice, amount
	if df['9MA'][t-1] > df['50MA'][t-1] and df['9MA'][t] < df['50MA'][t]: 
		choice = 'Sell'
		amount = stocks
		return choice, amount
	else:
		return 'none', 0

		
def Market(bank_account, stocks, df, amount):
	t = 0
	net = np.zeros((len(df['Adj Close'])))
	i = 0
	for t in range(len(df['Adj Close'])):
		net[t] = bank_account[i] + stocks[i][0]*df['Adj Close'][t]
		choice,amount = Agent_0(bank_account, stocks, df, t)
		if choice == 'Buy':
			stocks = stocks + amount
			bank_account[i] = bank_account[i] - amount*df['Adj Close'][t]
			net[t] = bank_account[i] + stocks[i][0]*df['Adj Close'][t]
		if choice == 'Sell':
			stocks = stocks - amount
			bank_account[i] = bank_account[i] + amount*df['Adj Close'][t]
			net[t] = bank_account[i] + stocks[i][0]*df['Adj Close'][t]
		else:
			net[t] = bank_account[i] + stocks[i][0]*df['Adj Close'][t]
	return bank_account, stocks, net,t
		
		
my_agents = [Agent_0, Agent_1]		
		
		
