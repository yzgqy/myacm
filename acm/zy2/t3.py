def reverse(list_input,klen):
    relist=[]
    k=[]
    for i in range (len(list_input)):
        k.append(list_input.pop(0))
        l_len=len(k)
        if l_len ==klen:
            for j in range(klen):
                relist.append(k.pop())
    for j in range(len(k)):
        relist.append(k.pop(0))
    return relist


if __name__ == '__main__':
    try:
        while True:
            arr = list(map(str, input().split()))
            k = int(arr[len(arr) - 1])
            arr = arr[1:len(arr)-1]
            arr = reverse(arr,k)
            print(" ".join(str(x) for x in arr))
    except:
        exit(0)