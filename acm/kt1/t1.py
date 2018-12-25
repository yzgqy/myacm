# Python3 program to find  minimum number
# of swaps required to sort an array

# Function returns the minimum
# number of swaps required to sort the array
def minSwaps(arr):
    n = len(arr)

    # Create two arrays and use
    # as pairs where first array
    # is element and second array
    # is position of first element
    # 创建两个数组，并作为对使用，其中第一个数组是元素，第二个数组是第一个元素的位置
    arrpos = [*enumerate(arr)]
    print(arrpos)
    # Sort the array by array element
    # values to get right position of
    # every element as the elements
    # of second array.
    # 按数组元素值对数组进行排序，以获得每个元素作为第二数组的元素的正确位置。
    arrpos.sort(key=lambda it: it[1])
    print(arrpos)

    # To keep track of visited elements.
    # Initialize all elements as not
    # visited or false.
    # 跟踪到访人员。将所有元素初始化为未访问或false。
    vis = {k: False for k in range(n)}

    # Initialize result
    ans = 0
    for i in range(n):

        # alreadt swapped or
        # alreadt present at
        # correct position
        # 交换或显示在正确位置
        if vis[i] or arrpos[i][0] == i:
            continue

        # find number of nodes
        # in this cycle and
        # add it to ans
        # 找到这个循环中的节点数，并将其添加到ans中
        cycle_size = 0
        j = i
        while not vis[j]:
            # mark node as visited
            # 标记该节点被访问
            vis[j] = True

            # move to next node
            # 移动到下一个节点
            j = arrpos[j][0]
            cycle_size += 1

        # update answer by adding
        # current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
            # return answer
    return ans


# Driver Code
arr = [1, 5, 4, 3, 2]
print(minSwaps(arr))

# This code is contributed
# by Dharan Aditya