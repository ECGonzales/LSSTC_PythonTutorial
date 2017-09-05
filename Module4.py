import pandas as pd
import numpy as np

df = pd.DataFrame({'int_col': [1, 2, 6, 8, -1], 'float_col': [0.1, 0.2, 0.2, 10.1, None],
                   'str_col': ['a', 'b', None, 'c', 'a']})

df2 = df.copy()                             # This command creates a copy of the original DataFrame
mean = df2['float_col'].mean()
df2['float_col'].fillna(mean,inplace=True)

df.describe()  # tells you a bunch of stats on the df

df['str_col'].dropna(inplace=True)
df['str_col'].map(lambda x: 'newvalue_'+x)  # this prints newvalue_a, etc only to the screen and not saved in the df
df[['int_col', 'float_col']].apply(np.sum)  # Get the sum for those two columns


def my_function(x):
 if type(x) is str:
      return 'my_string_function_' + x
 elif x:
      return np.sqrt(np.abs(x))
 else:
      return


 df.applymap(my_function)  # applymap only applies it to the df as an output and not perminately.
                           # Need to define as var to keep

df3 = pd.DataFrame({'int_col' : [1,2,6,8,-1], 'float_col' : [0.1, 0.2,0.3,10.1,4.0], 'str_col' : ['a','b','b','c','a']})
other =  pd.DataFrame({'str_col' : ['a','b'], 'some_val' : [1, 2]})
merge = pd.merge(df3,other,on='str_col',how='inner')  # merge on other's str_col
merge2 = pd.merge(df3,other,on='str_col',how='outer')  # merge on df3's str_col
merge3 = pd.merge(df3,other,on='str_col',how='left')  # merge on df3's str_col
merge4 = pd.merge(df3,other,on='str_col',how='right')  # merge on other's str_col




print('{:d} rows'.format(len(dat)))
print('{:.1f} MB'.format(dat.memory_usage(index=True,deep=True).sum()/1e6))

print(dat)