import warnings
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
from IPython.display import HTML
import time



##Importing and initializing the data (we are indexing by time(ms))
t0 = time.time()
print("started at "+str(t0))
print("Loading data")
data1 = pd.read_csv("TimeSeriesPull.csv")
data2 = pd.read_csv("TimeSeriesPull2.2.csv")
data3 = pd.read_csv("TimeSeriesPull3.2.csv")
data4 = pd.read_csv("TimeSeriesPull4.csv")
data5 = pd.read_csv("TimeSeriesPull5.csv")
data6 = pd.read_csv("TimeSeriesPull6.csv")
data7 = pd.read_csv("TimeSeriesPull7.csv")
data8 = pd.read_csv("TimeSeriesPull8.csv")
data9 = pd.read_csv("TimeSeriesPull9.csv")
data10 = pd.read_csv("TimeSeriesPull10.csv")
data11 = pd.read_csv("TimeSeriesPull11.csv")
data12 = pd.read_csv("TimeSeriesPull12.csv")
data13 = pd.read_csv("TimeSeriesPull13_2-WNAL11190.csv")
data14 = pd.read_csv("TimeSeriesPull14-WNAL11190.csv")
data15 = pd.read_csv("TimeSeriesPull15-WNAL11190.csv")
data16 = pd.read_csv("TimeSeriesPull16_2-WNAL11190.csv")
data17 = pd.read_csv("TimeSeriesPull17.csv")
data18 = pd.read_csv("TimeSeriesPull18-WNAL11190.csv")
data19 = pd.read_csv("TimeSeriesPull19.csv")
data20 = pd.read_csv("TimeSeriesPull20.csv")

print(str(time.time()-t0))
print("Creating Data Frames")
data_1 = pd.DataFrame(data1)
data_2 = pd.DataFrame(data2)
data_3 = pd.DataFrame(data3)
data_4 = pd.DataFrame(data4)
data_5 = pd.DataFrame(data5)
data_6 = pd.DataFrame(data6)
data_7 = pd.DataFrame(data7)
data_8 = pd.DataFrame(data8)
data_9 = pd.DataFrame(data9)
data_10 = pd.DataFrame(data10)
data_11 = pd.DataFrame(data11)
data_12 = pd.DataFrame(data12)
data_13 = pd.DataFrame(data13)
data_14 = pd.DataFrame(data14)
data_15 = pd.DataFrame(data15)
data_16 = pd.DataFrame(data16)
data_17 = pd.DataFrame(data17)
data_18 = pd.DataFrame(data18)
data_19 = pd.DataFrame(data19)
data_20 = pd.DataFrame(data20)
data = pd.concat([data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10,data_11,data_12, data_13, data_14, data_15, data_16, data_17, data_18, data_19, data_20], ignore_index=True)
data.rename(columns={'TagTime1':'Timestamp', 'TagValue':'Value'}, inplace=True)
data['Timestamp'] = pd.to_datetime(data['Timestamp'], unit='ms')
data = data.set_index('Timestamp')
print(str(time.time()-t0))
print("filtering data")

UniqueTags = data.TagName.nunique()
TagCount = data.TagName.count()
print("Unique Tag Names:" + str(UniqueTags))
print("Tag Count:" + str(TagCount))
print(data)


