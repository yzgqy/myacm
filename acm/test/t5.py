#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 4:27 PM
# @Author  : gqy
# @File    : t5.py
# @Software: PyCharm
# @Desc  :


if __name__ == '__main__':
    count = input()
    count = int(count)
    while count > 0:
        val = input()
        numlist = val.split(" ")
        n = int(numlist[0])
        sum = 0
        for x in range(1, len(numlist)):
            sum += int(numlist[x])
        print(sum)
        count -= 1