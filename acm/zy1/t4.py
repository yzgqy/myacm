#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 3:43 PM
# @Author  : gqy
# @File    : t4.py
# @Software: PyCharm
# @Desc  :
import time;
import sys;

#递归方式
def hanoiProblem1 (num, the_left, the_mid, the_right):
    if num < 1:
        return 0;
    else:
        return process(num, "left", "mid", "right", "left", "right")
def process(num, the_left, the_mid, the_right, the_from, the_to):
    if num == 1:
        if the_from == the_mid or the_to == the_mid:
            return 1
        else:
            return 2
    if the_from == the_mid or the_to == the_mid:
        another = ""
        if the_from == the_left or the_to == the_left:
            another = the_right
        else:
            another = the_left
        part1 = process(num - 1, the_left, the_mid, the_right,the_from, another)
        part2 = 1
        part3 = process(num - 1, the_left, the_mid, the_right, another, the_to)
        return part1 + part2 + part3;
    else:
        part1 = process(num - 1, the_left, the_mid, the_right,the_from, the_to)
        part2 = 1
        part3 = process(num - 1, the_left, the_mid, the_right, the_to,the_from)
        part4 = 1
        part5 = process(num - 1, the_left, the_mid, the_right,the_from, the_to)
        return part1 + part2 + part3 + part4 + part5


# 非递归的方法，用栈来模拟汉诺塔的三个塔
def hanoiProblem2(num, left, mid, right):
    lstack = []
    mstack = []
    rstack = []
    step = 0
    lstack.append(sys.maxsize)
    mstack.append(sys.maxsize)
    rstack.append(sys.maxsize)
    for i in range(num, 0, -1):
        lstack.append(i)
    record = ['No']
    while len(rstack) != num + 1:
        step += fStackTotStack(record, 'MToL', 'LToM', lstack, mstack,left, mid)
        step += fStackTotStack(record, 'LToM', 'MToL', mstack, lstack, mid, left)
        step += fStackTotStack(record, 'RToM', 'MToR', mstack, rstack, mid, right)
        step += fStackTotStack(record, 'MToR', 'RToM', rstack, mstack, right, mid)
    return step


def fStackTotStack(record,preNoAct,nowAct,fStack,tStack,the_from,the_to):
    if record[0] != preNoAct and fStack[-1] < tStack[-1]:
        tStack.append(fStack.pop())
        # print("Move " + str(tStack[-1]) + " from " + str(the_from) + " to " + str(the_to))
        record[0] = nowAct
        return 1
    return 0


def hanoi(num):
    return pow(3, num) - 1;


if __name__ == '__main__':
    num = int(input())
    start = time.time()
    print(hanoiProblem1(num, "left", "mid", "right"))
    end = time.time()
    print(str(end - start))
    # start = time.time()
    print(hanoiProblem2(num, "left", "mid", "right"))
    # end = time.time()
    # print(str(end - start))