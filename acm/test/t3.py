#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 3:34 PM
# @Author  : gqy
# @File    : t3.py
# @Software: PyCharm
# @Desc  :


if __name__ == '__main__':
    while True:
        val = input()
        numlist = val.split(" ")
        a = int(numlist[0])
        b = int(numlist[1])
        if a == 0 and b == 0:
            break
        print(a+b)