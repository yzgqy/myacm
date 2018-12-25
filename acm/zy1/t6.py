#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 3:14 PM
# @Author  : gqy
# @File    : t6.py
# @Software: PyCharm
# @Desc  :

def findConditionedNum(arr, sum_num):
    left = 0
    right = len(arr) - 1
    count = 0
    while left < right:
        if arr[left] + arr[right] == sum_num:
            count += 1
            right -= 1
        else:
            if arr[left] + arr[right] > sum_num:
                right -= 1
            elif arr[left] + arr[right] < sum_num:
                left += 1
    return count


if __name__ == '__main__':
    arr = list(map(int, input().split(" ")))
    sum_num = int(input())
    arr.sort(reverse=False)
    print(findConditionedNum(arr, sum_num))
