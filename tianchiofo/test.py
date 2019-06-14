import os, sys, pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from sklearn.linear_model import SGDClassifier, LogisticRegression

dfoff = pd.read_csv('ccf_offline_stage1_train.csv')
pd.set_option('display.max_columns', None)

df=dfoff
print(df)
#print(dfoff)
# print(dfoff.columns)
print(dfoff[dfoff['Date'].notnull()].groupby(['Date']).count())
#print(dfoff[(dfoff['Date'].notnull()) & (dfoff['Date_received'].notnull())])
#print(dfoff[(dfoff['Date'].notnull()) & (dfoff['Date_received'].notnull())][['Date_received', 'Date']])


