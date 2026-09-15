
import pandas as pd

std = [(1, 'zeenath', 30, 'female'),
       (2, 'faraz', 40, 'male'),
       (3, 'arham', 5, 'male'),
       (4, 'inaya', 3, 'female'), ]
df = pd.DataFrame(std, columns=['id', 'name', 'age', 'gender'])
print(df['age'])
print(df[['name','gender']])
print(df.loc[0])
print(df.loc[2])
print(df.iloc[0,2])
print(df.iloc[2,1])
print(df['age']>29)
#df['phone']=[10,20,30,40]
print(df)
#df=df.drop(columns=['phone'])
print(df)
df.insert(2,'phone',[10,20,30,40])
print(df)
df=df.rename(columns={'name':'names','age':'ages','gender':'genders'})
print(df)
del df['phone']
print(df)
#df=df.drop(3)
print(df)
df.loc[4]=[5,'lala',2,'male']
print(df)
df.loc[2,'ages']=7
print(df)
df.loc[[0,1],'ages']=[25,35]
print(df)