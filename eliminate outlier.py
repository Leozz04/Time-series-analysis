import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters

#package转换
register_matplotlib_converters()
#自输入filepath
filepath = input("Enter input filepath name: ")
input_path = Path(filepath)
data = pd.read_csv(filepath, header=0,
                   names=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volumn'], parse_dates=['Date'],
                   index_col=['Date'])
df = pd.DataFrame(data)
close = df.loc[:, ['Close']]
mean_price = close.mean()
std_price = close.std()
#z-test过滤掉一些过于离谱的outliers
z = pd.DataFrame((close - mean_price) / std_price)
thres = 1.645
outliers = pd.DataFrame(np.abs(z) > thres)
inner = (np.abs(z) <= thres).all(axis=1)
true_inner = pd.DataFrame(z[inner], dtype=float)
combined = pd.concat([close, true_inner], axis=1)
combined.columns = ['Close price', 'Inner']
#drop掉过滤值
rev_df = combined.dropna(subset='Inner', axis='index')
rev_df.columns = ['Close price', 'Inner']
#输出过滤后csv
output_path = input("Enter output directory path: ")
output_dir = Path(output_path)
output_dir.mkdir(parents=True, exist_ok=True)
#输出文件重名后缀改写
base_filename = input_path.stem + "_revised"
csv_suffix = ".csv"
plot_suffix = ".png"
csv_filename = base_filename + csv_suffix
csv_filepath = output_dir / csv_filename
counter = 1
while csv_filepath.exists():
    csv_filename = f"{base_filename}_{counter}{csv_suffix}"
    csv_filepath = output_dir / csv_filename
    counter += 1
rev_df.to_csv(csv_filepath)
#折线图绘制
fig, ax = plt.subplots()
ax.plot(rev_df.index.values, rev_df['Close price'])
ax.set(xlabel="Date", ylabel="Close price")
date_form = mdates.DateFormatter("%Y-%m")
ax.xaxis.set_major_formatter(date_form)
#折线图输出
plot_filename = base_filename + plot_suffix
plot_filepath = output_dir / plot_filename
counter = 1
while plot_filepath.exists():
    plot_filename = f"{base_filename}_{counter}{plot_suffix}"
    plot_filepath = output_dir / plot_filename
    counter += 1
plt.savefig(plot_filepath)

