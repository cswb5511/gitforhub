import pandas as pd

import numpy as np

import os


rootdir = '/Users/wangbo/Desktop/第二版数据/原始数据/56423/54623定时_visfcst_北京时间.txt'
# rootdir = '/Users/wangbo/Desktop/第二版数据/原始数据/56423/54623_test.txt'
# rootdir = '/Users/wangbo/Desktop/第二版数据/原始数据/56423/text.txt'
file_54623=open(rootdir,'r', encoding='gbk')
# file_54623=open(rootdir)
# 第一行的数据不要
line=file_54623.readline()
print(line)
df=pd.DataFrame()
line=file_54623.readline()

while line:
    mytest = [i for i in line.split(' ') if i != '']
    df=pd.concat([df,pd.DataFrame(mytest).T])
    line = file_54623.readline()
# print(mytest = [i for i in line.split(' ') if i != ''])
# while head:
#     print(head)
#     head = file_54623.readline()
df_date=df[1].str.cat(df[2],sep="-").str.cat(df[3],sep="-").str.cat(df[4],sep="-")
# df=df.drop([0],[1],[2],axis=1)
for i in range(5):
    df = df.drop([i],axis=1)

df=pd.concat([df_date,df],axis=1)
df.columns=['date','定时气压','定时气温','定时相对湿度','定时露点温度','定时风速','定时风速','定时自记降水','定时能见度']

df.to_csv('/Users/wangbo/Desktop/第二版数据/原始数据/56423/54623_data.csv',index=False)


