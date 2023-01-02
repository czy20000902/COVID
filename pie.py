import numpy as np
import matplotlib.pyplot as plt
import csv


def num(elem):
        return elem[1]

list = []
with open('1219.csv',encoding='utf-8') as csvfile:
        f_csv = csv.reader(csvfile)
        next(f_csv)
        for row in f_csv:
                list.append([row[0],int(row[3])])
#排序
list.sort(key=num,reverse=True)
pie_list=[]
#总数前十
for i in range(9):
        pie_list.append(list[i])
#other
other = 0
for i in range(9,len(list)):
        other+=list[i][1]
pie_list.append(['其他',other])

plt.figure(figsize=(20, 8), dpi=80)
plt.title("各个国家的累计确诊人数")
name = []
number = []
for i in range(len(pie_list)):
        name.append(pie_list[i][0])
        number.append(pie_list[i][1])
# 画出条形图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.pie(number,labels=name,autopct='%1.1f%%',shadow=False,startangle=90)
# plt.axis('equal')
plt.show()