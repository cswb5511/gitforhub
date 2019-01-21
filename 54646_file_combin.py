import numpy as np
import pandas as pd
import os

'''
初始化df包括head
'''

list_=['fct','u','v','w','pm2.5','pm10','height','tc','theta','rh']
head=[]

for i in list_:
    count = 1;
    while count<41:
        head.append(str(i)+'_'+str(count))
        count=count+1
count=2
# print(head)
for i in head:
    if(count<41):
        head.remove('fct_' + str(count))
        count = count + 1

# print(head)
df=pd.DataFrame(np.zeros((1,361)))
df.columns=['fct_1', 'u_1', 'u_2', 'u_3', 'u_4', 'u_5', 'u_6', 'u_7', 'u_8', 'u_9', 'u_10', 'u_11', 'u_12', 'u_13', 'u_14', 'u_15', 'u_16', 'u_17', 'u_18', 'u_19', 'u_20', 'u_21', 'u_22', 'u_23', 'u_24', 'u_25', 'u_26', 'u_27', 'u_28', 'u_29', 'u_30', 'u_31', 'u_32', 'u_33', 'u_34', 'u_35', 'u_36', 'u_37', 'u_38', 'u_39', 'u_40', 'v_1', 'v_2', 'v_3', 'v_4', 'v_5', 'v_6', 'v_7', 'v_8', 'v_9', 'v_10', 'v_11', 'v_12', 'v_13', 'v_14', 'v_15', 'v_16', 'v_17', 'v_18', 'v_19', 'v_20', 'v_21', 'v_22', 'v_23', 'v_24', 'v_25', 'v_26', 'v_27', 'v_28', 'v_29', 'v_30', 'v_31', 'v_32', 'v_33', 'v_34', 'v_35', 'v_36', 'v_37', 'v_38', 'v_39', 'v_40', 'w_1', 'w_2', 'w_3', 'w_4', 'w_5', 'w_6', 'w_7', 'w_8', 'w_9', 'w_10', 'w_11', 'w_12', 'w_13', 'w_14', 'w_15', 'w_16', 'w_17', 'w_18', 'w_19', 'w_20', 'w_21', 'w_22', 'w_23', 'w_24', 'w_25', 'w_26', 'w_27', 'w_28', 'w_29', 'w_30', 'w_31', 'w_32', 'w_33', 'w_34', 'w_35', 'w_36', 'w_37', 'w_38', 'w_39', 'w_40', 'pm2.5_1', 'pm2.5_2', 'pm2.5_3', 'pm2.5_4', 'pm2.5_5', 'pm2.5_6', 'pm2.5_7', 'pm2.5_8', 'pm2.5_9', 'pm2.5_10', 'pm2.5_11', 'pm2.5_12', 'pm2.5_13', 'pm2.5_14', 'pm2.5_15', 'pm2.5_16', 'pm2.5_17', 'pm2.5_18', 'pm2.5_19', 'pm2.5_20', 'pm2.5_21', 'pm2.5_22', 'pm2.5_23', 'pm2.5_24', 'pm2.5_25', 'pm2.5_26', 'pm2.5_27', 'pm2.5_28', 'pm2.5_29', 'pm2.5_30', 'pm2.5_31', 'pm2.5_32', 'pm2.5_33', 'pm2.5_34', 'pm2.5_35', 'pm2.5_36', 'pm2.5_37', 'pm2.5_38', 'pm2.5_39', 'pm2.5_40', 'pm10_1', 'pm10_2', 'pm10_3', 'pm10_4', 'pm10_5', 'pm10_6', 'pm10_7', 'pm10_8', 'pm10_9', 'pm10_10', 'pm10_11', 'pm10_12', 'pm10_13', 'pm10_14', 'pm10_15', 'pm10_16', 'pm10_17', 'pm10_18', 'pm10_19', 'pm10_20', 'pm10_21', 'pm10_22', 'pm10_23', 'pm10_24', 'pm10_25', 'pm10_26', 'pm10_27', 'pm10_28', 'pm10_29', 'pm10_30', 'pm10_31', 'pm10_32', 'pm10_33', 'pm10_34', 'pm10_35', 'pm10_36', 'pm10_37', 'pm10_38', 'pm10_39', 'pm10_40', 'height_1', 'height_2', 'height_3', 'height_4', 'height_5', 'height_6', 'height_7', 'height_8', 'height_9', 'height_10', 'height_11', 'height_12', 'height_13', 'height_14', 'height_15', 'height_16', 'height_17', 'height_18', 'height_19', 'height_20', 'height_21', 'height_22', 'height_23', 'height_24', 'height_25', 'height_26', 'height_27', 'height_28', 'height_29', 'height_30', 'height_31', 'height_32', 'height_33', 'height_34', 'height_35', 'height_36', 'height_37', 'height_38', 'height_39', 'height_40', 'tc_1', 'tc_2', 'tc_3', 'tc_4', 'tc_5', 'tc_6', 'tc_7', 'tc_8', 'tc_9', 'tc_10', 'tc_11', 'tc_12', 'tc_13', 'tc_14', 'tc_15', 'tc_16', 'tc_17', 'tc_18', 'tc_19', 'tc_20', 'tc_21', 'tc_22', 'tc_23', 'tc_24', 'tc_25', 'tc_26', 'tc_27', 'tc_28', 'tc_29', 'tc_30', 'tc_31', 'tc_32', 'tc_33', 'tc_34', 'tc_35', 'tc_36', 'tc_37', 'tc_38', 'tc_39', 'tc_40', 'theta_1', 'theta_2', 'theta_3', 'theta_4', 'theta_5', 'theta_6', 'theta_7', 'theta_8', 'theta_9', 'theta_10', 'theta_11', 'theta_12', 'theta_13', 'theta_14', 'theta_15', 'theta_16', 'theta_17', 'theta_18', 'theta_19', 'theta_20', 'theta_21', 'theta_22', 'theta_23', 'theta_24', 'theta_25', 'theta_26', 'theta_27', 'theta_28', 'theta_29', 'theta_30', 'theta_31', 'theta_32', 'theta_33', 'theta_34', 'theta_35', 'theta_36', 'theta_37', 'theta_38', 'theta_39', 'theta_40', 'rh_1', 'rh_2', 'rh_3', 'rh_4', 'rh_5', 'rh_6', 'rh_7', 'rh_8', 'rh_9', 'rh_10', 'rh_11', 'rh_12', 'rh_13', 'rh_14', 'rh_15', 'rh_16', 'rh_17', 'rh_18', 'rh_19', 'rh_20', 'rh_21', 'rh_22', 'rh_23', 'rh_24', 'rh_25', 'rh_26', 'rh_27', 'rh_28', 'rh_29', 'rh_30', 'rh_31', 'rh_32', 'rh_33', 'rh_34', 'rh_35', 'rh_36', 'rh_37', 'rh_38', 'rh_39', 'rh_40']




# 遍历文件夹

rootdir = '/Users/wangbo/Desktop/第二版数据/原始数据/54623high_part'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
list.sort()
# 定义一个最后拼接大表的df
df_full=pd.DataFrame()
for i in range(0,len(list)):
    path = os.path.join(rootdir,list[i])
    # 进入文件遍历循环
    if os.path.isfile(path):
        # fopen=open(path)
        # rootdir = '/Users/wangbo/Desktop/第二版数据/原始数据/54646/20170228.dat'


        df = pd.DataFrame()

        temp_list = []
        # temp_list.remove('a')
        file_open = open(path)
        date=path.split('/')[-1].split('.')[0]

        print(path)
        print(date)

        count = 0;
        for i in file_open:
            mytest = [i for i in i.split(' ') if i != '']
            if count % 10 == 0:
                if count==0:
                    pass
                else:
                    temp_list[0]=date+'_'+temp_list[0]

                df = pd.concat([df, pd.DataFrame(temp_list).T], axis=0)
                # print(temp_list)
                # print(temp_list.__len__())
                temp_list = []
            mytest.remove(mytest[0])
            temp_list = temp_list + mytest
            count = count + 1
            # print(temp_list)
            # print(temp_list.__len__())
            if (count == 240):
                temp_list[0] = date + '_' + temp_list[0]
                df = pd.concat([df, pd.DataFrame(temp_list).T], axis=0)

        df_full=pd.concat([df_full,df])



df_full.columns = ['fct_1', 'u_1', 'u_2', 'u_3', 'u_4', 'u_5', 'u_6', 'u_7', 'u_8', 'u_9', 'u_10', 'u_11', 'u_12',
                      'u_13', 'u_14', 'u_15', 'u_16', 'u_17', 'u_18', 'u_19', 'u_20', 'u_21', 'u_22', 'u_23', 'u_24',
                      'u_25', 'u_26', 'u_27', 'u_28', 'u_29', 'u_30', 'u_31', 'u_32', 'u_33', 'u_34', 'u_35', 'u_36',
                      'u_37', 'u_38', 'u_39', 'u_40', 'v_1', 'v_2', 'v_3', 'v_4', 'v_5', 'v_6', 'v_7', 'v_8', 'v_9',
                      'v_10', 'v_11', 'v_12', 'v_13', 'v_14', 'v_15', 'v_16', 'v_17', 'v_18', 'v_19', 'v_20', 'v_21',
                      'v_22', 'v_23', 'v_24', 'v_25', 'v_26', 'v_27', 'v_28', 'v_29', 'v_30', 'v_31', 'v_32', 'v_33',
                      'v_34', 'v_35', 'v_36', 'v_37', 'v_38', 'v_39', 'v_40', 'w_1', 'w_2', 'w_3', 'w_4', 'w_5', 'w_6',
                      'w_7', 'w_8', 'w_9', 'w_10', 'w_11', 'w_12', 'w_13', 'w_14', 'w_15', 'w_16', 'w_17', 'w_18',
                      'w_19', 'w_20', 'w_21', 'w_22', 'w_23', 'w_24', 'w_25', 'w_26', 'w_27', 'w_28', 'w_29', 'w_30',
                      'w_31', 'w_32', 'w_33', 'w_34', 'w_35', 'w_36', 'w_37', 'w_38', 'w_39', 'w_40', 'pm2.5_1',
                      'pm2.5_2', 'pm2.5_3', 'pm2.5_4', 'pm2.5_5', 'pm2.5_6', 'pm2.5_7', 'pm2.5_8', 'pm2.5_9',
                      'pm2.5_10', 'pm2.5_11', 'pm2.5_12', 'pm2.5_13', 'pm2.5_14', 'pm2.5_15', 'pm2.5_16', 'pm2.5_17',
                      'pm2.5_18', 'pm2.5_19', 'pm2.5_20', 'pm2.5_21', 'pm2.5_22', 'pm2.5_23', 'pm2.5_24', 'pm2.5_25',
                      'pm2.5_26', 'pm2.5_27', 'pm2.5_28', 'pm2.5_29', 'pm2.5_30', 'pm2.5_31', 'pm2.5_32', 'pm2.5_33',
                      'pm2.5_34', 'pm2.5_35', 'pm2.5_36', 'pm2.5_37', 'pm2.5_38', 'pm2.5_39', 'pm2.5_40', 'pm10_1',
                      'pm10_2', 'pm10_3', 'pm10_4', 'pm10_5', 'pm10_6', 'pm10_7', 'pm10_8', 'pm10_9', 'pm10_10',
                      'pm10_11', 'pm10_12', 'pm10_13', 'pm10_14', 'pm10_15', 'pm10_16', 'pm10_17', 'pm10_18', 'pm10_19',
                      'pm10_20', 'pm10_21', 'pm10_22', 'pm10_23', 'pm10_24', 'pm10_25', 'pm10_26', 'pm10_27', 'pm10_28',
                      'pm10_29', 'pm10_30', 'pm10_31', 'pm10_32', 'pm10_33', 'pm10_34', 'pm10_35', 'pm10_36', 'pm10_37',
                      'pm10_38', 'pm10_39', 'pm10_40', 'height_1', 'height_2', 'height_3', 'height_4', 'height_5',
                      'height_6', 'height_7', 'height_8', 'height_9', 'height_10', 'height_11', 'height_12',
                      'height_13', 'height_14', 'height_15', 'height_16', 'height_17', 'height_18', 'height_19',
                      'height_20', 'height_21', 'height_22', 'height_23', 'height_24', 'height_25', 'height_26',
                      'height_27', 'height_28', 'height_29', 'height_30', 'height_31', 'height_32', 'height_33',
                      'height_34', 'height_35', 'height_36', 'height_37', 'height_38', 'height_39', 'height_40', 'tc_1',
                      'tc_2', 'tc_3', 'tc_4', 'tc_5', 'tc_6', 'tc_7', 'tc_8', 'tc_9', 'tc_10', 'tc_11', 'tc_12',
                      'tc_13', 'tc_14', 'tc_15', 'tc_16', 'tc_17', 'tc_18', 'tc_19', 'tc_20', 'tc_21', 'tc_22', 'tc_23',
                      'tc_24', 'tc_25', 'tc_26', 'tc_27', 'tc_28', 'tc_29', 'tc_30', 'tc_31', 'tc_32', 'tc_33', 'tc_34',
                      'tc_35', 'tc_36', 'tc_37', 'tc_38', 'tc_39', 'tc_40', 'theta_1', 'theta_2', 'theta_3', 'theta_4',
                      'theta_5', 'theta_6', 'theta_7', 'theta_8', 'theta_9', 'theta_10', 'theta_11', 'theta_12',
                      'theta_13', 'theta_14', 'theta_15', 'theta_16', 'theta_17', 'theta_18', 'theta_19', 'theta_20',
                      'theta_21', 'theta_22', 'theta_23', 'theta_24', 'theta_25', 'theta_26', 'theta_27', 'theta_28',
                      'theta_29', 'theta_30', 'theta_31', 'theta_32', 'theta_33', 'theta_34', 'theta_35', 'theta_36',
                      'theta_37', 'theta_38', 'theta_39', 'theta_40', 'rh_1', 'rh_2', 'rh_3', 'rh_4', 'rh_5', 'rh_6',
                      'rh_7', 'rh_8', 'rh_9', 'rh_10', 'rh_11', 'rh_12', 'rh_13', 'rh_14', 'rh_15', 'rh_16', 'rh_17',
                      'rh_18', 'rh_19', 'rh_20', 'rh_21', 'rh_22', 'rh_23', 'rh_24', 'rh_25', 'rh_26', 'rh_27', 'rh_28',
                      'rh_29', 'rh_30', 'rh_31', 'rh_32', 'rh_33', 'rh_34', 'rh_35', 'rh_36', 'rh_37', 'rh_38', 'rh_39',
                      'rh_40']
print(df_full)




df_full.to_csv('/Users/wangbo/Desktop/第二版数据/原始数据/54623high_part/54623high_part_data_11_23.csv',index=False)




