if __name__ == '__main__':
    times = int(input())
    for i in range(times):
        n, m = list(map(int, input().split()))
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        countArr = [0 for i in range(m)]
        for i in range(n):
            for j in range(m):
                if arr1[i] % arr2[j] == 0:
                    countArr[j] += 1

        print(" ".join(str(i) for i in countArr))