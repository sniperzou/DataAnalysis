# -*- coding = utf-8 -*-
# @Time : 7/10/2022 16:01
# @Author : Jie
# @File : page89_2.py
# @Software : PyCharm
import numpy as np
from matplotlib import pyplot as plt

def main():
    us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
    uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

    # t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
    t_uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

    # 选择喜欢数比50w小的数据
    t_uk = t_uk[t_uk[:, 1] <= 500000]

    t_uk_comments = t_uk[:, -1]
    t_uk_likes = t_uk[:,  1]

    plt.figure(figsize=(20, 8), dpi=80)
    plt.scatter(t_uk_likes, t_uk_comments)

    plt.show()


if __name__ == "__main__":
    main()
