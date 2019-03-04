def is2k_arr(arr):
    sum1 = 0
    sum2 = 0
    if len(arr) % 2 ==0 :
        for i in range(len(arr)//2):
            sum1 += int(arr[i])
            sum2 += int(arr[len(arr)-i-1])
        if sum1 == sum2:
            return True
    return False


if __name__ == '__main__':
    times = int(input())
    for i in range(times):
        line = input()
        arr = list(line)
        count = len(arr)
        result = 0
        while count > 0:
            # print(count)
            if count % 2 == 0:
                for j in range(len(arr)-count+1):
                    # print("j :"+str(j))
                    # print(arr[0+j:count+j])
                    x = is2k_arr(arr[0+j:count+j])
                    if x:
                        result = count
                        break
                count -= 2
            else:
                count -= 1
            if result > 0:
                break
    print(result)