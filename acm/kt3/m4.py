if __name__ == '__main__':
    times = int(input())
    for i in range(times):
        txtstr, patstr = list(map(str, input().split(",")))
        txt = list(txtstr)
        pat = list(patstr)
        count = []
        flag = 0
        for i in range(len(txt) - len(pat)+1):
            if txt[i] == pat[0]:
                for j in range(1, len(pat)):
                    if txt[i+j] != pat[j]:
                        flag = 1
                        break
                if flag == 0:
                    count.append(i)
                else:
                    flag = 0
        print(" ".join(str(i) for i in count))