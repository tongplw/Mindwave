import numpy as np
import pandas as pd


df = pd.read_csv('data.csv')

df['power_2'] = 2 ** df['attention']
df['power_e'] = np.exp(df['attention'])
print(df.corr())