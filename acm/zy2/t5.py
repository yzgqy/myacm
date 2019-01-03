def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

if __name__ == '__main__':
    try:
        while True:
            arr = list(map(int, input().split()))
            arr = arr[1:]
            bubble_sort(arr)
            result = " ".join(str(x) for x in arr)
            print(result)
    except:
        exit(0)