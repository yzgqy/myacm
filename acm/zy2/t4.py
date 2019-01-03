def insert_sort(arr):
    length = len(arr)
    for i in range(1,length):
        x = arr[i]
        for j in range(i,-1,-1):
            # j为当前位置，试探j-1位置
            if x < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                # 位置确定为j
                break
        arr[j] = x

def printArr(arr):
    for item in arr:
        print(item)

if __name__ == '__main__':
    try:
        while True:
            arr = list(map(int, input().split()))
            arr = arr[1:]
            insert_sort(arr)
            result = " ".join(str(x) for x in arr)
            print(result)
    except:
        exit(0)
