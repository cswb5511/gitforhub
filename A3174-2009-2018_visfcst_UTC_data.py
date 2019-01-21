import pandas as pd

import numpy as np

import os

rootdir = '/Users/wangbo/Desktop/第二版数据/原始数据/56423/A3174-2009-2018_visfcst_UTC.txt'
# rootdir = '/Users/wangbo/Desktop/第二版数据/原始数据/56423/text.txt'
file_54423=open(rootdir)
# 前两行的sql数据不要
head=file_54423.readline()
head=file_54423.readline()
df=pd.DataFrame()
head=file_54423.readline()
while head:

    df=pd.concat([df,pd.DataFrame(head.split(' ')).T])
    head = file_54423.readline()
# 取高度值
df_8=df[7]
# 拼接日期
df=df[3].str.cat(df[4],sep="-").str.cat(df[5],sep="-").str.cat(df[6],sep="-")

# 组合大表
df=pd.concat([df,df_8],axis=1)
# 设置表头
df.columns=['date','miles']
df.to_csv('/Users/wangbo/Desktop/第二版数据/原始数据/56423/A3174-2009-2018_visfcst_UTC_data.csv',index=False)



