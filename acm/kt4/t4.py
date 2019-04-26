if __name__ == "__main__":
    t = int(input())
    ans = []
    for i in range(t):
        n = int(input())
        a = []
        for i in range(n):
            l = list(map(int, input().split()))
            m = []
            if i == 0:
                m = l
            else:
                m = [min(a[i - 1][2], a[i - 1][1]) + l[0], min(a[i - 1][0], a[i - 1][2]) + l[1],
                     min(a[i - 1][0], a[i - 1][1]) + l[2]]
            a.append(m)
        ans.append(min(a[-1]))
    for i in ans:
        print(i)