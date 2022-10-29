# -*- coding = utf-8 -*-
# @Time : 7/11/2022 16:54
# @Author : Jie
# @File : page122.py
# @Software : PyCharm


import pandas as pd
import numpy as np

def main():
    df = pd.read_csv('./IMDB-Movie-Data.csv')

    print(df.info())

    # 获取平均评分
    print(df['Rating'].mean())

    # 获取导演人数
    director_list = df['Director'].to_list()
    print(len(set(director_list)))
    print(len(df["Director"].unique()))


    # 获取演员的人数
    actors_list = df['Actors'].str.split(', ').tolist()
    # actors = [i.split(', ') for i in actors_list]
    # print(actors_list)
    # print(actors_list)
    actors = [actor for list in actors_list for actor in list]
    print(len(set(actors)))


if __name__ == "__main__":
    main()
