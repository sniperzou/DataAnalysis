# -*- coding = utf-8 -*-
# @Time : 8/2/2022 19:03
# @Author : Jie
# @File : 查找下行.py
# @Software : PyCharm
import re

import pandas as pd
import numpy as np

def main():
    df = pd.read_csv('./cut_file_list_1.csv')
    print(df.info())

    pattern = re.compile("draCtrlNrMdbfCe|draDlNrMdbfCe|upcUeDlNrCe")
    # pattern = re.compile("c$|h$|ifx")
    for indexs in df.index:
        file_str = df.loc[indexs, "file_list"]


        if pattern.search(file_str) is None:
            df.loc[indexs, "file_list"] = np.nan


    df.dropna(axis=0, how='any', inplace=True)
    print(df.info())
    df.to_csv('./dl_only.csv', index=None)


if __name__ == "__main__":
    main()
