import pandas as pd
import numpy as np

list=[1,2,3,4,2,1,2,3,4,1,12,3,2]
df=pd.DataFrame(list,columns=['scores'])
print(list)
#import txt with tabular delimiter
poke=pd.read_csv("pokemon_data.txt",delimiter='\t')
print(poke.head(2))
#get the column names of a data frame
#print(poke.columns)
#print names column for the first 5 rows
#print(poke["Attack"][0:5])
