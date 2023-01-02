import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model

list = [0] * 15
j = 0
for i in range(1205, 1220):  # 读入文件计算每日全球新增总量
        filename = '{}.csv'.format(str(i))
        df = pd.read_csv(filename)
        list[j] = int(df['累计'].sum())
        j += 1
# 训练集x1,y1
list1 = list[0:10]
list2 = list[10:15]
y1 = np.array(list1).reshape(-1, 1)
x1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
# 预测集x2
x2 = np.array([11, 12, 13, 14, 15]).reshape(-1, 1)
# Create linear regression object
regr = linear_model.LinearRegression()
regr.fit(x1, y1)
# 预测
predict_outcome = regr.predict(x2)
# 打印预测
print(predict_outcome)
# 打印截距
print({'截距': regr.intercept_})
# 打印系数
print({'系数': regr.coef_})

# 生成画布和子图
fig = plt.figure()
ax = fig.add_subplot()
# 设定支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 生成
ax.plot(np.arange(11, 16), predict_outcome, linewidth=2, linestyle="-", label='预测数据', marker='o')
ax.plot(np.arange(11, 16), list2, color='r', linewidth=2, linestyle="-", label='真实数据', marker='o')
plt.legend(loc='upper left', fontsize=7)
# 显示
plt.show()
