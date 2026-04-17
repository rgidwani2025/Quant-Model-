import yfinance as yf
import pandas as pd

data = yf.download('ES=F', start='2024-01-01', end='2024-12-31')
data.columns = data.columns.get_level_values(0)
data['SMA_20'] = data['Close'].rolling(window=20).mean()
print(data[['Close', 'SMA_20']].head(25))

data['Distance_to_SMA'] = abs(data['Close'] - data['SMA_20']) / data['SMA_20']
data['Touch'] = data['Distance_to_SMA'] < 0.01
data['Bounce_Up'] = (data['Close'].shift(-1) > data['Close']) & (data['Touch'])
data['Bounce_Down'] = (data['Close'].shift(-1) < data['Close']) & (data['Touch'])

print(data[['Close', 'SMA_20', 'Touch', 'Bounce_Up', 'Bounce_Down']].head(50))

print(data.head())

import matplotlib.pyplot as plt

plt.figure(figsize=(14, 6))
plt.plot(data.index, data['Close'], label='Close Price', linewidth=1)
plt.plot(data.index, data['SMA_20'], label='20-Day SMA', linewidth=2, color='orange')
plt.scatter(data[data['Bounce_Up'] == True].index, data[data['Bounce_Up'] == True]['Close'], color='green', label='Bounce Up', s=50)
plt.scatter(data[data['Bounce_Down'] == True].index, data[data['Bounce_Down'] == True]['Close'], color='red', label='Bounce Down', s=50)
plt.legend()
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('ES Futures with SMA and Bounce Signals')
plt.tight_layout()
plt.show()
