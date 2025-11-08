import pandas as pd

'''
Basic Usage and Conventions 
Pandas provides two main data structures: DataFrame and Series.
A Dataframe is a 2-D labeled data structure with columns 

A series is a 1-d labeled array
'''

#Creating a Series
data=[1, 2 ,3, 4,5]
print(type(data))
series=pd.Series(data)
print(series)
print(type(series))

#Creating DataFrame
data ={
    'Name': ['Alice','Bob','Charlie'],
    'Age':[25,30,40],
    'City':['New York', 'San Francisco','Los Angeles' ]
}

df= pd.DataFrame(data)
print(df)

print('head \n', df.head())
print('tail s-2 \n', df.tail())

print(df.info)
print('desc \n', df.describe())

#Select the columns
print(df['Name'])
print(df[['Name','City']])

#Filtering Rows
print(df[df['Age']>30])

#


