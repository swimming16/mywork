import pandas as pd
import numpy as np

#a = pd.DataFrame(np.random.randn(6,4), columns=['A','B','C','D'])
a=pd.DataFrame(np.random.randn(6,4))
print(a)
print(a.loc[1,2])#loc就是pandas的索引