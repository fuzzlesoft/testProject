import pandas as pd
#import txt with tabular delimiter
poke=pd.read_csv("pokemon_data.txt",delimiter='\t')
print(poke.head(5))
#get the column names of a data frame
print(poke.columns)
#print names column for the first 5 rows
print(poke["Name"][0:5])
#print rows 1-3 with Iloc function
print(poke.iloc[1:4])
#get a cell element by integer notaiton
print(poke.iloc[2][1])
#iterrows
for index, rows in poke.iterrows():
    print(index,rows["Name"])

    '''
    MORE ON ITERATING VIA LIST COMPREHENSIONS
    # Iterating over one column - `f` is some function that processes your data
        result = [f(x) for x in df['col']]
    # Iterating over two columns, use `zip`
        result = [f(x, y) for x, y in zip(df['col1'], df['col2'])]
    # Iterating over multiple columns - same data type
        result = [f(row[0], ..., row[n]) for row in df[['col1', ...,'coln']].to_numpy()]
    # Iterating over multiple columns - differing data type
        result = [f(row[0], ..., row[n]) for row in zip(df['col1'], ..., df['coln'])]
    
    
    
    '''


#finding rows by textual info
print(poke.loc[poke["Type 1"]=='Fire'])
#geting data from describe
print(poke.describe(include='all').loc[['mean',"std"]]["Generation"])
#sorting
print(poke.sort_values(["Name","Type 1"],ascending=[0,1]))
#creating a new column
#column is over all the rows and sums from columns 4:10 and it sums horizontally not down vertically
poke["total"] =poke.iloc[:,4:10].sum(axis=1)
#rearanging columns
cols=list(poke.columns.values)
poke=poke[cols[0:4]+[cols[-1]]+cols[4:12]]
#filtering data
poke.loc[(poke["Type 1"]=="Grass") & (poke["Type 2"]=="Poison") | (poke["HP"]>73)]

#getting rid of rows based on a condition
#gets rid of all rows with "Mega" in the "name" column
poke.loc[~poke["Name"].str.contains("Mega")]
#conditional changes
#poke of type 1 having fire will change second thing to the equals value
poke.loc[poke["Type 1"]=="Fire","Type 1"]="Flamer"
poke.loc[poke["Type 1"]=="Fire","Legendary"]=True
#if total is greater than 500 Gen to test 1 and Legendary to test 2
poke.loc[poke["total"]>500,["Generation","Legendary"]]=["Test 1","Test 2"]
#aggregate statistics
poke.groupby(["Type 1","Type 2"]).mean().sort_values("Defense")
poke.groupby(["Type 1","Type 2"]).sum()
poke.groupby(["Type 1","Type 2"]).count()
