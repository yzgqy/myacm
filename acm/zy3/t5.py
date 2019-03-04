def dfs(v, s, G):
    global mylen
    visited = [False] * v
    prev = [-1] * v
    recurDfs(s, visited, prev, G)
    # print(mylen)


def recurDfs(w, visited, prev, G):
    global mylen
    # print(mylen)
    visited[w] = True
    isEnd = True     #是否w所有的下个结点都被遍历过
    for x in G[w]:
        if not visited[x]:
            isEnd = False
        # isEnd = isEnd and visited[x]
    if isEnd:
        return
    for l in range(len(G[w])):
        q = G[w][l]
        if not visited[q]:
            prev[q] = w
            mylen += 1
            recurDfs(q, visited, prev, G)


def maxnum(m, n):
    if m > n:
        return m
    return n

if __name__ == '__main__':
    n = int(input())
    maxLen = 0
    for i in range(n):
        mylen = 1
        G = []
        line1 = list(input().split())
        v = int(line1[0])  #个数
        sStr = line1[1]  #开始点
        nodes = list(input().split())
        sIndex = -1;  # 开始点编号
        for j in range(len(nodes)):
            if nodes[j] == sStr:
                sIndex = j
                break
        for k in range(v):
            line = list(input().split())
            line.pop(0)
            linkLine = []
            for h in range(len(line)):
                # print(line[h])
                if int(line[h]) == 1:
                    linkLine.append(h)
            G.append(linkLine)
        # print(G)
        dfs(v, sIndex, G)
        # print(mylen)
        maxLen = maxnum(maxLen, mylen)
    print(maxLen)


