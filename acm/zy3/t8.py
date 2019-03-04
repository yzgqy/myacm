def get_point_num(labels):
    temp=[]
    for item in labels:
        if item not in temp:
            temp.append(item)
    temp.sort()
    return len(temp),temp

def is_exists(indegrees):
    tmp=0
    for n in indegrees:
        if (indegrees[n] == 0):
            tmp+=1
    return tmp

def get_index(item,temp):
    for i in range(len(temp)):
        if(str(temp[i])==str(item)):
            return i

def topu_sort(indegrees,edges,visited,nodes,path,result,count):
    for i in range(len(indegrees)):
        #未被标记且入度为0
        if(visited[nodes[i]]==0 and indegrees[nodes[i]]==0):
            path.append(nodes[i])
            visited[nodes[i]]=1
            for j in range(len(edges)):
                if(str(edges[j][0])==str(nodes[i])):
                    indegrees[edges[j][1]]-=1
            topu_sort(indegrees,edges,visited,nodes,path,result,count)
            if (len(path)!=0):
                # print("path=", path)
                count+=1
                # print("result1=",result)
                result.append(path)
                # print("result2=", result)
                path.clear()

            visited[nodes[i]] = 0
            for j in range(len(edges)):
                if(str(edges[j][0])==str(nodes[i])):
                    indegrees[edges[j][1]]+=1
    return len(result)


casenum=int(input())
list1=[]

for i in range(casenum):
    list1.append(input())

for j in range(len(list1)):
    edges = []
    labels = []
    # indegrees存放每个顶点的入度
    indegrees = {}
    arr=list1[j].split(",")
    for i in range(len(arr)):
        temp=arr[i].split()
        labels.append(temp[0])
        labels.append(temp[1])
        edges.append((temp[0],temp[1]))
    point_num,tmp=get_point_num(labels)
    for n in range(0,point_num):
        indegrees[tmp[n]]=0
        for m in range(len(edges)):
            if(str(edges[m][1])==str(tmp[n])):
                indegrees[tmp[n]]+=1
    visited={}
    for i in range(0,point_num):
        visited[tmp[i]]=0
    path=[]
    result=[]
    num=0
    num = topu_sort(indegrees, edges, visited, tmp, path, result, num)
    print(num)
