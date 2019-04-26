def dfs(w):
    global ans
    global cd
    global wt
    if cd[w] == 0:
        return w;
    if wt[w] < ans:
        ans = wt[w]
    return dfs(cd[w])

def solve(graph):
    global ans
    global cd
    global wt
    global rd
    global a
    global b
    global c
    global n
    global p
    i = 0
    # print(p)
    while i < p:
        q = graph[i][0]
        h = graph[i][1]
        t = graph[i][2]

        cd[q] = h
        wt[q] = t
        rd[h] = q
        i += 1
    for j in range(n):
        if rd[j] == 0 and cd[j] > 0:
            ans =100000000;
            w = dfs(j)
            # putLine = str(j) + ' ' + str(w) + ' ' + str(ans)
            # print(putLine)
            a.append(j)
            b.append(w)
            c.append(ans)
    print(len(a))
    for k in range(len(a)):
        putLine = str(a[k]) +' '+str(b[k])+' '+str(c[k])
        print(putLine)

if __name__ == "__main__" :
    n = int(input())
    for i in range(n):
        numb = list(map(int, input().split()))
        n = numb[0]
        p = numb[1]
        graph = []
        rd=[0 for i in range(1100)]
        wt=[0 for i in range(1100)]
        cd=[0 for i in range(1100)]
        a=[]
        b=[]
        c=[]
        ans=0
        x = p
        while x > 0:
            edge = list(map(int, input().split()))
            graph.append(edge)
            x -= 1
        # print(graph)
        solve(graph)
