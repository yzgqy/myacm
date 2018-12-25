def first(arr, low, high, x, n):
    if high >= low:
        mid = low + (high - low) // 2
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        if x > arr[mid]:
            return first(arr, (mid + 1), high, x, n)
        return first(arr, low, (mid - 1), x, n)
    return -1

def sortByArr(A1, A2, m, n):
    # 存储A1的副本
    temp = [0] * m
    # 标记temp中是否被访问
    visited = [0] * m
    for i in range(0, m):
        temp[i] = A1[i]
        visited[i] = 0
    temp.sort()
    index = 0

    for i in range(0, n):
        # 查找在temp中首次出现A2[i]的下标
        f = first(temp, 0, m - 1, A2[i], m)
        # 如果不存在，则不需要继续进行
        if f == -1:
            continue
        # 将temp中出现的所有A2[i]复制到A1[]
        j = f
        while j < m and temp[j] == A2[i]:
            A1[index] = temp[j]
            index = index + 1
            # 标记访问
            visited[j] = 1
            j = j + 1

    # 复制A2[]中不存在的所有temp[]到Ai中
    for i in range(0, m):
        # 未被访问
        if visited[i] == 0:
            A1[index] = temp[i]
            index = index + 1

# 打印结果
def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")
    print("")

if __name__ == '__main__':
    times = int(input())
    for x in range(0, times):
        count = list(map(int, input().split(" ")))
        arr1 = list(map(int, input().split(" ")))
        arr2 = list(map(int, input().split(" ")))
        m = count[0]
        n = count[1]
        sortByArr(arr1, arr2, m, n)
        printArray(arr1, m)
