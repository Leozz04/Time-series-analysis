import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import WindowsPath
from pandas import DataFrame

filepath = input("Enter input filepath name: ")
data = pd.read_csv(filepath, header=0,
                   names=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volumn'])
df = pd.DataFrame(data)
close = df.loc[:, ['Close']]
Date = df.loc[:, ['Date']]
mean_price = close.mean()
std_price = close.std()
z = pd.DataFrame((close - mean_price) / std_price)
thres = 1.645
outliers = pd.DataFrame(np.abs(z) > thres)
inner = (np.abs(z) <= thres).all(axis=1)
true_inner = pd.DataFrame(z[inner], dtype=float)

combined: DataFrame = pd.concat([Date, close, true_inner], axis=1)
combined.columns = ['Date', 'Close price', 'Inner']
combined['Date'] = pd.to_datetime(combined['Date'], format='%Y-%m-%d')
combined_df = pd.DataFrame(combined)

output_path = input("Enter output filepath name: ")
path = WindowsPath(output_path + '\\output.csv')
path.parent.mkdir(parents=True, exist_ok=True)
combined_df.to_csv(path)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plot = ax.plot(combined['Date'], combined['Close price'])
plt.savefig(output_path + r'\plot.png')





