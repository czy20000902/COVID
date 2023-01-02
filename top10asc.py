import numpy as np
import matplotlib.pyplot as plt
import csv

list = []
for i in range(10):
        list.append([])
for i in range(10):
        for j in range(15):
                list[i].append(0)
name = ['美国', '土耳其', '巴西', '印度', '俄罗斯', '德国', '英国', '意大利', '法国', '乌克兰']

date = 0
for index in range(1205, 1220):
        file_path = index.__str__() + '.csv'
        with open(file_path, encoding='utf-8') as csvfile:
                f_csv = csv.reader(csvfile)
                next(f_csv)
                for row in f_csv:
                        for i in range(10):
                                if row[0] == name[i]:
                                        list[i][date] = int(row[1])
                date += 1

# 横坐标
x = np.array(range(1205, 1220))
# 同时创建图像喝坐标轴实例
fig, ax = plt.subplots()
# 设置坐标轴标签
ax.set_xlabel("日期")
ax.set_ylabel("人数")
# 设定标题
ax.set_title("每日新增曲线图")
# 设定支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 隐藏边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
# x的刻度
ax.set_xticks(x)
# 画出折线
for i in range(10):
        plt.plot(x, list[i], linewidth=2, linestyle="-", label=name[i])
# 图例
plt.legend(loc='upper right', fontsize=7)
# 展示
plt.show()
