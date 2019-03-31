from __future__ import print_function
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D'])
df2=pd.DataFrame(np.arange(12).reshape(4,-1),index=['a','b','c','d'])#-1 for compute col aotuly
print(df2)
print(df2[:,['2']])
print(df)
print(df['A'], df.A)#two writing styles are same
print(df[0:3])
print(df['20130102':'20130104'])#two writing styles are same

# select by label: loc
print(df.loc['20130102'])
print(df.loc[:,['A','B']])
print(df.loc['20130102', ['A','B']])

# select by position: iloc
print(df.iloc[3])
print(df.iloc[3, 1])
print(df.iloc[3:5,0:2])
print(df.iloc[[1,2,4],[0,2]])

# mixed selection: ix
print(df.ix[:3, ['A', 'C']])
# Boolean indexing
print(df[df.A > 0])