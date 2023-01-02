import numpy as np
import matplotlib.pyplot as plt
import csv

list = [[], [], [], [], []]
list[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list[1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list[2] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list[3] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list[4] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
type = ['新增', '现有', '累计', '治愈', '死亡']
date = 0
name = 1205
for index in range(1205, 1220):
        file_path = index.__str__() + '.csv'
        with open(file_path, encoding='utf-8') as csvfile:
                f_csv = csv.reader(csvfile)
                next(f_csv)
                for row in f_csv:
                        list[0][date] += int(row[1])
                        list[1][date] += int(row[2])
                        list[2][date] += int(row[3])
                        list[3][date] += int(row[4])
                        list[4][date] += int(row[5])
                date += 1

# 横坐标
x = np.array(range(1205, 1220))
# 颜色列表
list_color = ['yellow', 'red', 'black', 'green', 'blue']
# 同时创建图像喝坐标轴实例
fig, ax = plt.subplots()
# 设置坐标轴标签
ax.set_xlabel("日期")
ax.set_ylabel("人数")
# 设定标题
ax.set_title("全球疫情曲线图")
# 设定支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 隐藏边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
# x的刻度
ax.set_xticks(x)
# 画出折线
for i in range(5):
        plt.plot(x, list[i], color=list_color[i], linewidth=2, linestyle="-", label=type[i])
# 图例
plt.legend(loc='upper right', fontsize=7)
# 展示
plt.show()
