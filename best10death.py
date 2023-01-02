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
                list.append([row[0], float(row[5]) / float(row[3])])

for elem in list:
        if elem[1] >= 1:
                elem[1] = 0
        if elem[1] < 0:
                elem[1] = 0
list.sort(key=num, reverse=False)
plt.figure(figsize=(20, 8), dpi=80)
plt.title("死亡率最低的 10 个国家")
name = []
y = []
for i in range(10):
        name.append(list[i][0])
        y.append(list[i][1])
# 放进横坐标的数字列表
x = range(10)
print(name)
print(y)
# 画出条形图
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.ylim(0, 1)
plt.bar(x, y, width=0.5)

# 修改刻度名称
plt.xticks(x, name)
plt.show()
