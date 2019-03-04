# import sys

def bfs(arr,ind,start):
    result = ''
    q = []
    startNode = ind.index(start)
    result += start
    result += ' '
    q.append(startNode)
    m = q[0]

    while len(q) != 0:
        for i in range(1,len(G[m])):
            if G[m][i] == '1':
                if ind[i-1] not in result:
                    result += ind[i-1]
                    result += ' '
                    q.append(i-1)
        q.pop(0)
        if len(q) != 0:
            m = q[0]

    return result


n = int(input())

while n>0:
    start = list(map(str, input().split()))
    ind = list(map(str, input().split()))

    rows = int(start[0])
    startCh = start[1]

    G = []
    for i in range(rows):
        G.append(list(map(str, input().split())))

    res = bfs(G,ind,startCh)

    print (res)
    n -= 1