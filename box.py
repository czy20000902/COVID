import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

df = pd.read_csv('1219.csv', encoding='utf-8')
plt.figure(figsize=(20, 8), dpi=80)
plt.title("全球各个国家累计确诊人数")
# 设置支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 画出箱型图
df.boxplot(column='累计', showmeans=True)
plt.show()
