def chess(tr, tc, pr, pc, size,table):
    if size == 1:
        return
    half = size // 2
    a = tr + half - 1
    b = tr + half
    c = tc + half - 1
    d = tc + half

    if pr < tr + half and pc < tc + half:
        table[a][d] = str(b)+" "+str(c)+","+str(b)+" "+str(d)
        table[b][c] = str(a)+" "+str(d)+","+str(b)+" "+str(d)
        table[b][d] = str(a)+" "+str(d)+","+str(b)+" "+str(c)
        chess(tr, tc, pr, pc, half,table)
    else:
        chess(tr, tc, tr + half - 1, tc + half - 1, half,table)

    if pr < tr + half and pc >= tc + half:
        table[a][c] = str(b) + " " + str(c) + "," + str(b) + " " + str(d)
        table[b][c] = str(a) + " " + str(c) + "," + str(b) + " " + str(d)
        table[b][d] = str(a) + " " + str(c) + "," + str(b) + " " + str(c)
        chess(tr, tc + half, pr, pc, half,table)
    else:
        chess(tr, tc + half, tr + half - 1, tc + half, half,table)

    if pr >= tr + half and pc < tc + half:
        table[a][c] = str(a) + " " + str(d) + "," + str(b) + " " + str(d)
        table[a][d] = str(a) + " " + str(c) + "," + str(b) + " " + str(d)
        table[b][d] = str(a) + " " + str(c) + "," + str(a) + " " + str(d)
        chess(tr + half, tc, pr, pc, half,table)
    else:
        chess(tr + half, tc, tr + half, tc + half - 1, half,table)

    if pr >= tr + half and pc >= tc + half:
        table[a][c] = str(a) + " " + str(d) + "," + str(b) + " " + str(c)
        table[a][d] = str(a) + " " + str(c) + "," + str(b) + " " + str(c)
        table[b][c] = str(a) + " " + str(c) + "," + str(a) + " " + str(d)
        chess(tr + half, tc + half, pr, pc, half,table)
    else:
        chess(tr + half, tc + half, tr + half, tc + half, half,table)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        line1 = list(map(int, input().split()))
        line2 = list(map(int, input().split()))
        pr = line1[1]
        pc = line1[2]
        n = line1[0]
        x = line2[0]
        y = line2[1]
        size = int(pow(2, n))
        table = [[-1 for x in range(size)] for y in range(size)]
        chess(0, 0, pr, pc, size, table)
        print(table[x][y])