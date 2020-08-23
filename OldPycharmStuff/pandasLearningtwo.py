import numpy as np
import pandas as pd
#loading a hardcoded data frame
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])


df=pd.read_csv("Fremont_weather.txt")
print(df)
print(df.dtypes)
print(df.index)
print(df.columns)
print(df.values)
for index, row in df.iterrows():
    print(index, row["month"],row["avg_high"])

print(df[df.avg_precipitation>1.0])
print(df[df['month'].isin(["Jun",'Jul'])])

df.loc[9,["avg_precipitation"]]=101.3
print(df.iloc[9:12])


# 9. assignment -- very similar to slicing

df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])


df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])


df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())


df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns

df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())


df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())