def ShellInsertSort(Lst,step_arr):
    Llen = len(Lst)
    for step in step_arr:
        for i in range(0, step):
            k = i+step
            while k < Llen:
                value = Lst[k]
                j = k - step
                while j >= 0:
                    if Lst[j] > value:
                        Lst[j + step] = Lst[j]
                    else:
                        break
                    j -= step
                Lst[j + step] = value
                k += step
    return Lst


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        Lst = list(map(int, input().split()))
        step_arr = list(map(int, input().split()))
        arr = ShellInsertSort(Lst, step_arr)
        print(" ".join(str(i) for i in arr))

