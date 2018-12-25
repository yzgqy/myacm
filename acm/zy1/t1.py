def getNum1(arr, num):
    if arr == None or len(arr) == 0:
        return 0
    qmin = []
    qmax = []
    i = 0
    j = 0
    res = 0
    while i < len(arr):
        while j < len(arr):
            while qmin and arr[qmin[-1]] >= arr[j]:
                qmin.pop()
            qmin.append(j)
            while qmax and arr[qmax[-1]] <= arr[j]:
                qmax.pop()
            qmax.append(j)
            if arr[qmax[0]] - arr[qmin[0]] > num:
                break
            j += 1
        if qmin[0] == i:
            qmin.pop(0)
        if qmax[0] == i:
            qmax.pop(0)
        res += j - i
        i += 1
    return res

def getNum(arr, num):
    if (len(arr) == 0):
        return 0
    L = 0
    R = 0
    res = 0
    qmax = []
    qmin = []

    while (L < len(arr)):
        while (R < len(arr)):
            while (len(qmax) != 0 and arr[R] >= arr[qmax[len(qmax) - 1]]):
                qmax.pop()
            qmax.append(R)

            while (len(qmin) != 0 and arr[R] <= arr[qmin[len(qmin) - 1]]):
                qmin.pop()
            qmin.append(R)

            if (arr[qmax[0]] - arr[qmin[0]] > num):
                break
            R = R + 1
        res += (len(arr) - R)
        if (qmax[0] == L):
            qmax.pop(0)
        if (qmin[0] == L):
            qmin.pop(0)
        L = L + 1
    return res




if __name__ == '__main__':
    arr = list(map(int, input().split()))

    num = int(input())
    print(getNum(arr, num))
