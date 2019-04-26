# import sys
#
# def maximizeSum(a, n) :
#    ans = dict.fromkeys(range(0, n + 1), 0)
#    for i in range(n):
#       ans[a[i]] += 1
#
#    print(ans)
#    maximum = max(a)
#
#    for i in range(2, maximum + 1) :
#       ans[i] = max(ans[i - 1],ans[i - 2] + ans[i] * i)
#
#    print(ans)
#    return ans[maximum]
#
#
# if __name__ == "__main__" :
#
#     T = int(input())
#     while T > 0:
#         l = int(input())
#         a = list(map(int,sys.stdin.readline().strip().split()))
#         # n = len(a)
#         print(maximizeSum(a, l))

import sys

def solve(a,l):
    if l == 0:return 0
    elif l == 1: return a[l-1]
    else:
        x = a[l-1]
        ind = a.index(x)
        if ind == l-1:
            a.pop()
            a.pop()
            l -= 2
        else:
            if ind != 0:
                a.pop(ind-1)
                a.pop(ind-1)
                l -= 2
            else :
                a.pop(ind)
                l -= 1

        x += solve(a, l)
        return x

if __name__ == "__main__" :
    n = int(input())
    for x in range(n):
    # while n > 0:
        l = int(input())
        a = list(map(int, input().split()))
        print(solve(a, l))
        # n -= 1
