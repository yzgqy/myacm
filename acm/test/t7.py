#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 4:42 PM
# @Author  : gqy
# @File    : t7.py
# @Software: PyCharm
# @Desc  :


if __name__ == '__main__':
    first = 1
    while True:
        val = input()
        numlist = val.split(" ")
        a = int(numlist[0])
        b = int(numlist[1])
        if first == 1:
            first = 0
        else:
            print(" ")
        print(a + b)