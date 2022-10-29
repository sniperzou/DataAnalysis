# -*- coding = utf-8 -*-
# @Time : 7/10/2022 15:47
# @Author : Jie
# @File : page89.py
# @Software : PyCharm
import numpy as np
from matplotlib import pyplot as plt

def main():
    us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
    uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

    # t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
    t_us = np.loadtxt(us_file_path, delimiter=",", dtype="int")
    t_us_comments = t_us[:,-1]

    print(t_us_comments.max(), t_us_comments.min())

    t_us_comments = t_us_comments[t_us_comments <= 5000]
    print(t_us_comments.max(), t_us_comments.min())
    d = 50
    bin_nums = (t_us_comments.max() - t_us_comments.min()) // d

    # 绘图
    plt.figure(figsize=(20,8), dpi=80)
    plt.hist(t_us_comments, bin_nums)

    plt.show()




if __name__ == "__main__":
    main()
