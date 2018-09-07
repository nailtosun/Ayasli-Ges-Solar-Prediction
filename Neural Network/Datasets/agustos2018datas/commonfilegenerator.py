import pandas as pd
dates = range(180801,180822)
filelist = []
for date in dates:
    filelist.append('min'+str(date)+'.csv')
