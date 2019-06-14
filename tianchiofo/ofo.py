import os, sys, pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from sklearn.linear_model import SGDClassifier
pd.set_option('display.max_columns', None)


dfoff = pd.read_csv('ccf_offline_stage1_train.csv')
dftest = pd.read_csv('ccf_offline_stage1_test_revised.csv')
print(dfoff.head(5))

print('有优惠卷，购买商品：%d' % dfoff[(dfoff['Date_received'].notnull()) & (dfoff['Date'].notnull())].shape[0])
print('有优惠卷，未购商品：%d' % dfoff[(dfoff['Date_received'].notnull()) & (dfoff['Date'].isnull())].shape[0])
print('无优惠卷，购买商品：%d' % dfoff[(dfoff['Date_received'] .isnull()) & (dfoff['Date'] .notnull())].shape[0])
print('无优惠卷，未购商品：%d' % dfoff[(dfoff['Date_received'] .isnull()) & (dfoff['Date'] .isnull())].shape[0])

print(dfoff["Discount_rate"].unique())

print(dfoff["Distance"].unique())

# 1. 将满xx减yy类型(`xx:yy`)的券变成折扣率 : discount_rate=1 - yy/xx
# discount_man, discount_jian是将满减的类型分开如100:20则discount_man=100,discount_jian=20

# convert Discount_rate and Distance
def getDiscountType(row):
    if pd.isnull(row):
        return np.nan

    elif ':' in row:
        return 1
    else:
        return 0

def convertRate(row):
    """Convert discount to rate"""
    if pd.isnull(row):
        return 1.0
    elif ':' in str(row):
        rows = row.split(':')
        return 1.0 - float(rows[1])/float(rows[0])
    else:
        return float(row)

def getDiscountMan(row):
    if ':' in str(row):
        rows = row.split(':')
        return int(rows[0])
    else:
        return 0

def getDiscountJian(row):
    if ':' in str(row):
        rows = row.split(':')
        return int(rows[1])
    else:
        return 0

def processData(df):
    # convert discunt_rate
    df['discount_rate'] = df['Discount_rate'].apply(convertRate)
    df['discount_man'] = df['Discount_rate'].apply(getDiscountMan)
    df['discount_jian'] = df['Discount_rate'].apply(getDiscountJian)
    df['discount_type'] = df['Discount_rate'].apply(getDiscountType)
    #print(df['discount_rate'].unique())#所有不同的折扣率
    # convert distance
    df['distance'] = df['Distance'].fillna(-1).astype(int)
    return df
#print(dfoff)
dfoff = processData(dfoff)
#print(dfoff)
dftest = processData(dftest)

date_received = dfoff['Date_received'].unique()
date_received = sorted(date_received[pd.notnull(date_received)])
print(date_received)

date_buy = dfoff['Date'].unique()
date_buy = sorted(date_buy[pd.notnull(date_buy)])
date_buy = sorted(dfoff[dfoff['Date'].notnull()]['Date'])

date_received = dfoff[dfoff['Date_received'].notnull()][['Date_received', 'Date']].groupby(['Date_received'], as_index=False).count()
date_received.columns = ['Date_received','count']
buybydate = dfoff[(dfoff['Date'].notnull()) & (dfoff['Date_received'].notnull())][['Date_received', 'Date']].groupby(['Date_received'], as_index=False).count()
buybydate.columns = ['Date_received','count']

print(buybydate) #按日期统计使用了优惠券消费的人群的数量

print("end")

# 提取星期的特征,weekday,
# weekday_type :  周六和周日为1，其他为0
# 将星期的特征编码为one-hot形式,增加七个特征

def getWeekday(row):
    if row == 'nan':
        return np.nan
    else:
        return date(int(row[0:4]), int(row[4:6]), int(row[6:8])).weekday() + 1

dfoff['weekday'] = dfoff['Date_received'].astype(str).apply(getWeekday)
dftest['weekday'] = dftest['Date_received'].astype(str).apply(getWeekday)

# weekday_type :  周六和周日为1，其他为0
dfoff['weekday_type'] = dfoff['weekday'].apply(lambda x : 1 if x in [6,7] else 0 )
dftest['weekday_type'] = dftest['weekday'].apply(lambda x : 1 if x in [6,7] else 0 )
print(dfoff['weekday_type'])

# change weekday to one-hot encoding
weekdaycols = ['weekday_' + str(i) for i in range(1,8)]
tmpdf = pd.get_dummies(dfoff['weekday'].replace('nan', np.nan))
tmpdf.columns = weekdaycols
dfoff[weekdaycols] = tmpdf

tmpdf = pd.get_dummies(dftest['weekday'].replace('nan', np.nan))
tmpdf.columns = weekdaycols
dftest[weekdaycols] = tmpdf


#有了特征之后，我们还需要对训练样本进行 label 标注，即确定哪些是正样本（y = 1），哪些是负样本（y = 0)

#没有领优惠券,标记为-1,无效
def label(row):
    if pd.isnull(row['Date_received']):
        return -1
#15天内使用优惠券 标记为1
    if pd.notnull(row['Date']):
        td = pd.to_datetime(row['Date'], format='%Y%m%d') -  pd.to_datetime(row['Date_received'], format='%Y%m%d')
        if td <= pd.Timedelta(15, 'D'):
            return 1
    return 0
dfoff['label'] = dfoff.apply(label, axis = 1)
print(dfoff)
print(dfoff['label'].value_counts())
print("end")

# data split
print("-----data split------")
df = dfoff[dfoff['label'] != -1].copy()
train = df[(df['Date_received'] < 20160530)].copy()
valid = df[(df['Date_received'] >= 20160530) & (df['Date_received'] <= 20160630)].copy()
print("end")

# feature
original_feature = ['discount_rate','discount_type','discount_man', 'discount_jian','distance', 'weekday', 'weekday_type'] + weekdaycols
print("----train-----")
model = SGDClassifier(#lambda:
    loss='log',
    penalty='elasticnet',
    fit_intercept=True,
    max_iter=100,
    shuffle=True,
    alpha = 0.01,
    l1_ratio = 0.01,
    n_jobs=1,
    class_weight=None
)
# model.fit(train[original_feature], train['label'])
#
# # #### 预测以及结果评价
# print(model.score(valid[original_feature], valid['label']))
#
# ##保存模型
# print("---save model---")
# with open('1_model.pkl', 'wb') as f:
#     pickle.dump(model, f)
# with open('1_model.pkl', 'rb') as f:
#     model = pickle.load(f)
#
# # test prediction for submission
# y_test_pred = model.predict_proba(dftest[original_feature])
# print(y_test_pred)
# dftest1 = dftest[['User_id','Coupon_id','Date_received']].copy()
# dftest1['label'] = y_test_pred[:,1]
# dftest1.to_csv('submit1.csv', index=False, header=False)
# print(dftest1.head())