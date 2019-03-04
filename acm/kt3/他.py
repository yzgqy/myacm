import sys

num = int(input())
while (num > 0):
    maxLenth = 0
    numStr = sys.stdin.readline().strip()
    # arr = list(map(int, numStr.split()))
    arr = []
    for c in numStr:
        arr.append(int(c))

    for i in range(len(arr)-1):
        j = i+1
        left = 0
        right = 0
        lenth = 0
        while (i >= 0 and j <= len(arr)-1):
            left += arr[i]
            right += arr[j]
            if (left == right):
                lenth = j-i+1
                if(lenth > maxLenth): maxLenth = lenth
            i -= 1
            j += 1
    print(maxLenth)
    num -= 1