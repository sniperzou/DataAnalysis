# coding=utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np
my_font = font_manager.FontProperties(fname=r"C:\Users\ejizoji\AppData\Local\Microsoft\Windows\Fonts\方正北魏楷书简体.ttf")

y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]


np_y1 = np.array(y_1)
np_y2 = np.array(y_2)

max_y1 = np.argmax(np_y1)
min_y1 = np.argmin(np_y1)

max_y2 = np.argmax(np_y2)
min_y2 = np.argmin(np_y2)

x = range(11,31)

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y_1,label="自己",color="#F08080")
plt.plot(x,y_2,label="同桌",color="#DB7093",linestyle="--")

plt.plot(max_y1 + 11, np_y1[max_y1], 'ks')

fig, ax = plt.subplots()

plt.rcParams['font.sans-serif']=['SimHei']

fig.text(0.75, 0.45, "我的花花世界",
         fontsize=40, color='grey',
         ha='right', va='bottom', alpha=0.4)


show_y1_max = f'[{max_y1} {np_y1[max_y1]}]'
# plt.annotate(show_y1_max, xytext=(max_y1 + 11, np_y1[max_y1]), xy=(max_y1 + 11, np_y1[max_y1]))
plt.annotate(show_y1_max, xy=(max_y1 + 11, np_y1[max_y1]))
#设置x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels,fontproperties=my_font)
# plt.yticks(range(0,9))

#绘制网格
plt.grid(alpha=0.4,linestyle=':')

#添加图例
plt.legend(prop=my_font,loc="upper left")

#展示
plt.show()
