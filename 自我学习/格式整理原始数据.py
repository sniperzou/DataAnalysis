# -*- coding = utf-8 -*-
# @Time : 8/2/2022 19:17
# @Author : Jie
# @File : 格式整理原始数据.py
# @Software : PyCharm
import os.path
import re

import pandas as pd
import numpy as np
import datetime

def main():
    df = pd.read_csv('./HZ87363.csv')
    # df.info()
    # df.head(1)
    today = datetime.date.today()

    if not os.path.exists(f'./{today}'):
        os.makedirs(f'./{today}')

    total_num = 80

    df = df.iloc[:total_num]
    for indexs in df.index:
        file_str = df.loc[indexs, "file_list"]
        df.loc[indexs, "file_list"] = file_str.replace(";", "\n")
        # print(df.loc[indexs, "file_list"])

    print(df.info())
    df.to_csv(f'./{today}/diff_commit_file_list_origin_0~{total_num}.csv', index=None)

    pattern = re.compile("xml$|yaml$|test|Test|env|deployment|bzl$")
    # pattern = re.compile("c$|h$|ifx")
    for indexs in df.index:
        file_str = df.loc[indexs, "file_list"]
        file_list = file_str.split("\n")
        # print(file_list)
        new_file_list = []
        for file in file_list:
            if pattern.search(file) is None:
                new_file_list.append(file)
        # print(new_file_list)
        if len(new_file_list) == 0:
            df.loc[indexs, "file_list"] = np.nan
        else:
            df.loc[indexs, "file_list"] = "\n".join(new_file_list)


    df.dropna(axis=0, how='any', inplace=True)
    print(df.info())
    print(df.head(5))
    df.to_csv(f'./{today}/cut_file_list_0~{total_num}.csv', index=None)


    pattern = re.compile("draCtrlNrMdbfCe|draDlNrMdbfCe|upcUeDlNrCe")
    # pattern = re.compile("c$|h$|ifx")
    for indexs in df.index:
        file_str = df.loc[indexs, "file_list"]


        if pattern.search(file_str) is None:
            df.loc[indexs, "file_list"] = np.nan


    df.dropna(axis=0, how='any', inplace=True)
    print(df.info())
    df.to_csv(f'./{today}/dl_only_0~{total_num}.csv', index=None)



if __name__ == "__main__":
    main()
