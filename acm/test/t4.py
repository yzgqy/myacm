#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 4:23 PM
# @Author  : gqy
# @File    : t4.py
# @Software: PyCharm
# @Desc  :

while True:
    val = input()
    try:
        numlist = val.split(" ")
        n = int(numlist[0])
        if n == 0:
            break
        sum = 0
        for x in range(1, len(numlist)):
            sum += int(numlist[x])
        print(sum)
    except:
        exit(0)

