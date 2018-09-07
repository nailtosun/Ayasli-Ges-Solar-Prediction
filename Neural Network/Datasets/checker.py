import pandas as pd
df = pd.read_csv('epoch_time_vs_SumPac.csv',sep = ';',header=None)
missing_values = []
for i in range(len(df)-1):
    if df[0][i] - df[0][i+1] != 300:
        missing_values.append(df[1][i])
        print(i)
missing_values
