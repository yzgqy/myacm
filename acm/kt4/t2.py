# def getMaxNum(arr , size):
#     max_list = []
#     # for j in range(0, size):
#     #     max_list.append(0)
#     i = 0
#     for x in arr:
#         if x > 0:
#             if len(max_list) == 0:
#                 max_list.append(x)
#             else:
#                 if max_list[i] < 0:
#                     max_list.append(x)
#                     i += 1
#                 else:
#                     max_list[i] += x
#         else:
#             max_list.append(x)
#             i += 1
#     print(max_list)
#     return max(max_list)
#
#
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         line1 = int(input())
#         line2 = list(map(int, input().split()))
#         min_one = 0
#         index = -1
#         for j in range(0, line1):
#             if line2[j] < 0 and min_one > line2[j]:
#                 min_one = line2[j]
#                 index = j
#         print(min_one)
#         print(index)
#         max_sum = 0
#         if index > -1:
#             line2.pop(index)
#             max_sum = getMaxNum(line2, line1-1)
#         else:
#             max_sum = getMaxNum(line2,line1)
#         print(getMaxNum(line2, line1))
#
#         print(max_sum)


def maxSumSubarray(arr, n):
    fw = [arr[i] for i in range(n)]
    bw = [arr[i] for i in range(n)]
    for i in range(1, n):
        fw[i] = max(fw[i], fw[i]+fw[i-1])
    for i in range(n-2, -1, -1):
        bw[i] = max(bw[i], bw[i]+bw[i+1])
    ans = arr[0]
    for i in range(n):
        if fw[i] == bw[i]:
            ans = max(ans, fw[i])
        else:
            ans = max(ans, fw[i]+bw[i]-(2*arr[i]), fw[i]+bw[i]-arr[i])
    return(ans)


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxSumSubarray(arr, n))