
# -*- coding: utf-8 -*-

import pandas as pd
f=open('./data/class_data/test.csv','rb')
# read 4 file
novel_yule=pd.read_csv(f,encoding='gb18030')
f=open('./data/class_data/test_xuanyi.csv','rb')
novel_xuanyi=pd.read_csv(f,encoding='gb18030')
f=open('./data/class_data/xuanyi_words.csv','rb')
xuanyi_words=pd.read_csv(f,encoding='gb18030',header=None)
f=open('./data/class_data/yule_words.csv','rb')
yule_words=pd.read_csv(f,encoding='gb18030',header=None)

combin_key_xuanyi=(xuanyi_words[1]+'_'+xuanyi_words[2])
# 为了对应计数字典的字典 key=查询的热词 value=分类。
dit=dict(zip(xuanyi_words[0],combin_key_xuanyi))

combin_key_xuanyi=(xuanyi_words[1]+'_'+xuanyi_words[2]).drop_duplicates()

# 用来计数的字典key=分类 value=list[展示量，展示用户，点击量，用户点击量]
dit_xuanyi={}

xuanyi_list=list(combin_key_xuanyi)


for i in range(list(combin_key_xuanyi).__len__()):

    dit_xuanyi[xuanyi_list[i]]=[0,0,0,0]

f=open('./data/class_data/test_xuanyi.csv',encoding='gb18030')
line=f.readline()
line=f.readline()
while line:
    tmp_list=line.split(',')
    if ';' in tmp_list[0]:
        tmp_list_words=tmp_list[0].split(';')
        for i in range(tmp_list_words.__len__()):
            if tmp_list_words[i] in dit.keys():
                tmp_values=dit_xuanyi.get(dit.get(tmp_list_words[i]))
                dit_xuanyi[dit.get(tmp_list_words[i])]=[tmp_values[0]+int(tmp_list[1])
                    ,tmp_values[1]+int(tmp_list[2])
                    ,tmp_values[2]+int(tmp_list[3])
                    ,tmp_values[3]+int(tmp_list[4])]
    else:
        if tmp_list_words[i] in dit.keys():
            tmp_values = dit_xuanyi.get(dit.get(tmp_list_words[i]))
            dit_xuanyi[dit.get(tmp_list_words[i])] = [tmp_values[0] + int(tmp_list[1])
                , tmp_values[1] + int(tmp_list[2])
                , tmp_values[2] + int(tmp_list[3])
                , tmp_values[3] + int(tmp_list[4])]
    line=f.readline()


f.close()
print(dit_xuanyi)

if __name__ == '__main__':
    dit={'a':1,'b':2}
    dit['a']=dit.get('a')+10
    print(dit)


