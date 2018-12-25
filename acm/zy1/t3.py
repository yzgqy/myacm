#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 4:35 PM
# @Author  : gqy
# @File    : t3.py
# @Software: PyCharm
# @Desc  :

def slide(arr,w):
    result = 0;
    if len(arr) == 0 or len(arr) < w:
        return result
    # 滑动窗口队列
    queue = []
    for i in range(len(arr)):
        # 如果队列不为空并且队列最后一个元素小于等于当前数时循环：将最大的放到队首
        while len(queue) != 0 and arr[queue[-1]] <= arr[i]:
            # 移除最后一个
            queue.pop(-1)
        # 加入队列
        queue.append(i)
        # 判断队首元素是否起作用，最大的那个是否已经过去
        if queue[0] == i-w:
            queue.pop(0)
        # 累加最大元素
        if i >= w-1:
            # print(arr[queue[0]])
            result += arr[queue[0]]
    return result


if __name__ == '__main__':
    # arr = [4, 3, 5, 4, 3, 3, 6, 7]
    # print(slide(arr, 3))
    arr = list(map(int, input().split(" ")))
    w =int(input())
    print(slide(arr, w))