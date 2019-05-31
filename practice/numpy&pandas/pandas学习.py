import pandas as pd
import numpy as np

#a = pd.DataFrame(np.random.randn(6,4), columns=['A','B','C','D'])
a=pd.DataFrame(np.random.randn(6,4),columns=['A','B','C','D'])
print(a)

#iloc根据位置索引，loc根据位置的名称索引
print(a.iloc[1,2])#loc就是pandas的索引
