import pandas as pd
from datetime import datetime

df =  pd.read_csv(r'2806-10-05.csv',sep = ';',header=None)
datetime_object = []
for i in range(len(df)):
    datetime_object.append(df[0][i]+ ' ' +df[1][i])

epoch_time = []
for i in range(len(df)):
    datetime = datetime.strptime(datetime_object[i], '%d.%m.%Y %H:%M:%S')
    epoch = datetime.timestamp()                                            #Turn into local time
    epoch_time.append(epoch)

missing_values = []
for i in range(len(df)-1):
    if epoch_time[i] - epoch_time[i+1] != 300:
        missing_values.append(datetime.fromtimestamp(epoch_time[i]))
missing_values
epoch_time_2 = pd.DataFrame(epoch_time)
epoch_time_2.to_csv('epoch2.csv', index = False)
a = df[2]
a.to_csv('timedata2.csv',index=False)
len(epoch_time)
