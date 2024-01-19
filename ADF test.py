import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
data = pd.read_csv('/Users/Leo/Downloads/combined.csv')
df = data['Close price']
plt.figure(figsize=(10, 6))
plt.plot(df, label='Closing Prices')
plt.title('Intel Corporation Stock Prices')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

def perform_adf_test(series):
    result = adfuller(series, autolag='AIC')
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    print('Critical Values:')
    for key, value in result[4].items():
        print(f'\t{key}: {value}')

# Apply ADF test on the series
perform_adf_test(df)
