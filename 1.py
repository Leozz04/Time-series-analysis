import numpy as np
import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.api as sm
from arch.unitroot import ADF
from arch.unitroot import PhillipsPerron

input_path = Path(r'C:\Users\ziqia\PycharmProjects\Time series analysis\AAPL_revised.csv')
data = pd.read_csv(input_path,
                   header=0,
                   names=['Close price', 'Inner'])
acf = plot_acf(data['Close price'])
pacf = plot_pacf(data['Close price'], lags=50)

output_dir = Path(r'C:\Users\ziqia\PycharmProjects\Time series analysis')

acf_name = input_path.stem + " ACF"
pacf_name = input_path.stem + " PACF"
plot_suffix = ".png"
acf_filename = acf_name + plot_suffix
acf_filepath = output_dir / acf_filename
pacf_filename = pacf_name + plot_suffix
pacf_filepath = output_dir / pacf_filename
plt.savefig(acf_filepath)
plt.savefig(pacf_filepath)


def describe(X):
    split = int(len(X) / 2)
    X1, X2 = X[0:split], X[split:]
    mean1, mean2 = X1.mean(), X2.mean()
    var1, var2 = X1.var(), X2.var()
    print('mean1=%f, mean2=%f' % (mean1, mean2))
    print('variance1=%f, variance2=%f' % (var1, var2))


print('price')
describe(data['Close price'])

adf = ADF(data['Close price'])
print(adf.summary().as_text())

adf = ADF(data['Close price'])
adf.trend = 'ct'
print(adf.summary().as_text())

pp = PhillipsPerron(data['Close price'])
print(pp.summary().as_text())

pp = PhillipsPerron(data['Close price'])
pp.trend = 'ct'
print(pp.summary().as_text())
