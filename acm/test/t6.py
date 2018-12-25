#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 4:31 PM
# @Author  : gqy
# @File    : t6.py
# @Software: PyCharm
# @Desc  :


# if __name__ == '__main__':
while True:
    try:
        val = input()
        numlist = val.split(" ")
        n = int(numlist[0])
        sum = 0
        for x in range(1, len(numlist)):
            sum += int(numlist[x])
        print(sum)
    except:
        exit(0)

