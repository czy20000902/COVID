import numpy as np
import matplotlib.pyplot as plt
import csv


def num(elem):
        return elem[1]


list = []
with open('1219.csv', encoding='utf-8') as csvfile:
        f_csv = csv.reader(csvfile)
        next(f_csv)
        for row in f_csv:
                list.append([row[0], float(row[3])])
with open('population.csv', encoding='gbk') as csvfile:
        f_csv = csv.reader(csvfile)
        for row in f_csv:
                for elem in list:
                        if elem[0] == row[0]:
                                if elem[0] == '印度':
                                        print(elem)
                                        print(row)
                                elem[1] = elem[1] / float(row[1])
                # print(elem)

for elem in list:
        if elem[1] >= 1:
                elem[1] = 0
list.sort(key=num, reverse=True)
plt.figure(figsize=(20, 8), dpi=80)
plt.title("累计确诊人数占国家总人口比例最高的10个国家")
name = []
y = []
for i in range(10):
        name.append(list[i][0])
        y.append(list[i][1])
# 放进横坐标的数字列表
x = range(10)
print(name)
# 画出条形图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(x, y, width=0.5)

# 修改刻度名称
plt.xticks(x, name)
plt.show()
