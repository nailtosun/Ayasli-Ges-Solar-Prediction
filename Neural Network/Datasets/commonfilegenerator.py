import pandas as pd
from datetime import datetime
dates = range(180801,180822)
filelist = []
for date in dates:
    filelist.append('agustos2018datas\min' + str(date)+'.csv')
df = pd.read_csv(filelist[0],sep=';')
df['Time'][0]+df['Time']
SumPac = []
Date = []
i = 0
df['Pac'][i]+df['Pac.2'][i]+df['Pac.3'][i]+df['Pac.4'][i]+df['Pac.5'][i]+df['Pac.6'][i]+df['Pac.7'][i]+df['Pac.8'][i]+df['Pac.9'][i]+df['Pac.1'][i]
for file in filelist:
    df = pd.read_csv(file,sep=';')
    for i in range(len(df)):
        SumPac.append(df['Pac'][i]+df['Pac.2'][i]+df['Pac.3'][i]+df['Pac.4'][i]+df['Pac.5'][i]+df['Pac.6'][i]+df['Pac.7'][i]+df['Pac.8'][i]+df['Pac.9'][i]+df['Pac.1'][i])
        Date.append(str((df['#Date'][i]) + ' ' + df['Time'][i]))

epoch_time = []
Date[0]
for i in range(len(Date)):
    datetime = datetime.strptime(Date[i], '%d.%m.%y %H:%M:%S')
    epoch = datetime.timestamp()                                            #Turn into local time
    epoch_time.append(epoch)
df_wrote = pd.DataFrame(epoch_time)
df_wrote.to_csv('agustos_missing_epoch.csv',index=False)
# %%
df1 = pd.read_csv('agustos2.csv' ,sep = ';',header = None)
missing_values = []
for i in range(len(df1)-1):
    if df1[0][i] - df1[0][i+1] != 300:
        missing_values.append(df1[0][i])
        print(i)
missing_values
len(df1)/288
