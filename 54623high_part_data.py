import pandas as pd

import numpy as np

import os




rootdir = '/Users/wangbo/Desktop/第二版数据/原始数据/54623-surface'
# rootdir = '/Users/wangbo/Desktop/第二版数据/原始数据/测试文件夹'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
list.sort()
# 定义一个最后拼接大表的df
df_full=pd.DataFrame()
for i in range(0,len(list)):
    path = os.path.join(rootdir,list[i])
    # 进入文件遍历循环
    if os.path.isfile(path):
        # 遍历文件夹
        df_temp = pd.read_csv(path, sep='\s+', header=None)
        df_temp = pd.concat([pd.DataFrame([path.split('/')[-1].split('.')[0]+'-']*24),df_temp],axis=1)

        df_temp.columns=['0','1','2','3','4','5','6','7','8','9','10','11']
        df_full=pd.concat([df_full,df_temp],ignore_index=True)


# print(df_full)

df_full.to_csv('/Users/wangbo/Desktop/第二版数据/原始数据/54623-surface/54623-surface-data.csv',index=False)
