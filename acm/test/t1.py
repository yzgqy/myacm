#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 3:17 PM
# @Author  : gqy
# @File    : t1.py
# @Software: PyCharm
# @Desc  :


if __name__ == '__main__':
    while True:
        val = input()
        numlist = val.split(" ")
        a = int(numlist[0])
        b = int(numlist[1])
        print(a+b)

    # count = input()
    # count = int(count)
    # while count > 0:
    #     val = input()
    #     numlist = val.split(" ")
    #     a = int(numlist[0])
    #     b = int(numlist[1])
    #     print(a+b)
    #     count -= 1
