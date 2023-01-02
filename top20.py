import numpy as np
import matplotlib.pyplot as plt
import csv


def num(elem):
        return elem[1]


list = []
with open('1205.csv', encoding='utf-8') as csvfile:
        f_csv = csv.reader(csvfile)
        next(f_csv)
        for row in f_csv:
                list.append([row[0], int(row[3])])
with open('1219.csv', encoding='utf-8') as csvfile:
        f_csv = csv.reader(csvfile)
        next(f_csv)
        for row in f_csv:
                for l in list:
                        if l[0] == row[0]:
                                l[1] = int(row[3]) - l[1]
list.sort(key=num, reverse=True)
plt.figure(figsize=(20, 8), dpi=80)

name = []
y = []
for i in range(20):
        name.append(list[i][0])
        y.append(list[i][1])
# 放进横坐标的数字列表
x = range(20)
print(name)
# 画出条形图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(x, y, width=0.5, color=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'g'])
plt.title('累计新增确诊数排名前20名的国家')
# 修改刻度名称
plt.xticks(x, name)
plt.show()
