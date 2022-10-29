# -*- coding = utf-8 -*-
# @Time : 8/2/2022 17:30
# @Author : Jie
# @File : pd_test.py
# @Software : PyCharm
import re

import pandas as pd
import numpy as np


def main():
    df = pd.read_csv('./HZ87363.csv')
    # print(df.info())
    # print(df.head(1))

    # file_list = df['file_list'].to_list()
    # print(file_list[:-1])

    # for row in df.iterrows():
    #     print(row[1])

    pattern = re.compile("xml$|yaml$|test|Test|env|deployment|bzl$")
    # pattern = re.compile("c$|h$|ifx")
    for indexs in df.index:
        file_str = df.loc[indexs, "file_list"]
        file_list = file_str.split(";")
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
    df.to_csv('./cut_file_list_1.csv', index=None)



if __name__ == "__main__":
    main()
