import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import copy
from matplotlib import style
import csv
import time
import calendar
import datetime

plt.style.use('ggplot')

start = dt.datetime(1970, 01, 01)
end = dt.datetime(2019, 02, 20)
order = True
ticker = '^GSPC'

df = web.DataReader(ticker, 'yahoo', start, end)

df['50_MA'] = df['Adj Close'].rolling(window = 50, min_periods = 50).mean()
df['200_MA'] = df['Adj Close'].rolling(window = 200, min_periods = 200).mean()

cycle = 'none'
count = 0
period = [(0,0,0,0),(0,0,0,0)]*12
duration = [0]*int(len(period))
recession = [8,124,687,34,445,98,56,453,222,7,236,88,161,149,70,7,926,79,55,550,112,172,115,105]
while order == True:
	for t in range(len(df)):
		if df['50_MA'][t] < df['200_MA'][t] and cycle != 'enter':
			cycle = 'enter'
			enter_date = df.index[t]
			enter_points = df['Adj Close'][t]
			count = count +1
			print cycle, df.index[t]
		if df['50_MA'][t] > df['200_MA'][t] and cycle == 'enter':
			cycle = 'exit'
			exit_date = df.index[t]
			exit_points = df['Adj Close'][t]
			period[count-1] = enter_date, enter_points, exit_date, exit_points
			enter_date = 0
			enter_points = 0
			print cycle, df.index[t]
			
	order = False


print count
cycles = [0]*int(len(recession))

for i in range(len(duration)):
	duration[i] = period[i][2] - period[i][0]
	cycles[i] = i + 1
	print duration[i], period[i][0], period[i][2]

start = [0]*len(period)
for i in range(len(start)):
	start[i] = period[i][0]

t = np.arange(1970, 2018, 1)

plt.bar(start, recession, width = 80, color = 'royalblue')
plt.xlabel('Year')
plt.ylabel('# of days')
plt.title('Historical duration of the death cross cycles')
plt.show()

# ~ timestamp = int(time.mktime(datetime.now().timetuple()))
# ~ print timestamp
# ~ now = datetime.fromtimestamp(timestamp)
# ~ print now
