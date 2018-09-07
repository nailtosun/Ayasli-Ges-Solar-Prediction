import pandas as pd
from datetime import datetime
df =  pd.read_csv(r'anan.csv',sep = ';',header=None, dtype={0: object})
df.head()
datetime_object = []
for i in range(len(df)):
    datetime_object.append(str(df[0][i])+ ' ' +df[1][i])
datetime_object[3000]
epoch_time = []
for i in range(len(df)):
    datetime = datetime.strptime(datetime_object[i], '%d%m%y %H:%M:%S')
    epoch = datetime.timestamp()                                            #Turn into local time
    epoch_time.append(epoch)
missing_values = []
len(df)
len(epoch_time)
epoch_time[3000]
for i in range(len(df)-1):
    if epoch_time[i] - epoch_time[i+1] != 300:
        missing_values.append(datetime.fromtimestamp(epoch_time[i]))

missing_values
# %%
missing_day_list = []
counter = 0
for i in range(len(df)-1):
    if df[0][i] == df[0][i+1]:
        counter = counter + 1
    else:
        if counter != 287:
            missing_day_list.append(df[0][i])
            print(i)
        counter  = 0
missing_day_list
len(epoch_time)
patates = df[2]
epoch_time_df = pd.DataFrame(epoch_time)
epoch_time_df.to_csv('epoch3.csv',index=False)
