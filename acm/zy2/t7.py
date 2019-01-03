def quick_sort(arr):
    '''''
    模拟栈操作实现非递归的快速排序
    '''
    if len(arr) < 2:
        return arr
    stack = []
    stack.append(len(arr)-1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)


def partition(arr, start, end):
    # 分区操作，返回基准线下标
    pivot = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    # 此时start = end
    arr[start] = pivot
    return start

if __name__ == '__main__':
    try:
        while True:
            arr = list(map(int, input().split()))
            arr = arr[1:]
            quick_sort(arr)
            result = " ".join(str(x) for x in arr)
            print(result)
    except:
        exit(0)

# if __name__=='__main__':
#     allList=[]
#     while(True):
#         numStr = input();
#         if(numStr==""):
#             break
#         a =list(map(int,numStr.split()))
#         allList.append(a)
#     for a in allList:
#         if a[0] !=0:
#             a =a[1:]
#             a =quick_sort(a)
#             print(" ".join(str(i) for i in a))
#         else:
#             print('')
