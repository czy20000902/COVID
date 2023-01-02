import numpy as np
import matplotlib.pyplot as plt
import csv


list = [0]*15
date = 0
for index in range(1205,1220):
        file_path=index.__str__()+'.csv'
        with open(file_path,encoding='utf-8') as csvfile:
                f_csv = csv.reader(csvfile)
                next(f_csv)
                for row in f_csv:
                        list[date] += int(row[3])
                date += 1

# 横坐标
x = np.array(range(1205, 1220))
# 同时创建图像喝坐标轴实例
fig, ax = plt.subplots()
# 设置坐标轴标签
ax.set_xlabel("日期")
ax.set_ylabel("人数")
# 设定标题
ax.set_title("全球累计确诊曲线图")
# 设定支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 隐藏边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
# x的刻度
ax.set_xticks(x)
# 画出折线
plt.plot(x, list, linewidth=2, linestyle="-")
# 图例
plt.legend(loc='upper right', fontsize=7)
# 展示
plt.show()
