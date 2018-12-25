def minSwaps(n, arr):
    # n = len(arr)
    # 将原数组转化为（下标，数值）的数组
    arrpos = list(enumerate(arr))
    # 按数组元素值对数组进行排序
    arrpos.sort(key=lambda it: it[1])
    # 标记数组元素是否被访问，初始为未被访问
    vis = {k: False for k in range(n)}
    ans = 0
    for i in range(n):
        # 如果被访问了或者位置没有变化，跳过
        if vis[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            # 标记该节点被访问
            vis[j] = True
            # 移动到交换位置的地方
            j = arrpos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans

if __name__ == '__main__':
    # arr = [1, 5, 4, 3, 2]
    # print(minSwaps(arr))
    times = int(input())
    for x in range(0, times):
        n = int(input())
        sqe = input()
        arr = list(map(int, sqe.split(" ")))
        print(minSwaps(n, arr))
