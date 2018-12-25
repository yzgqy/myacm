# int LIS(int *array,int len)
def longest_increasing_subsequence(arr):
    arr_len = len(arr)
    LIS = [0 for i in range(arr_len)];
    max = 1
    LIS[0] = arr[0]
    for i in range(arr_len):
        left = 0
        right = max
        while left <= right:
            mid = (left+right)//2
            if LIS[mid] < arr[i]:
                left = mid + 1
            else:
                right = mid - 1
        LIS[left] = arr[i]
        if left > max:
            max += 1
    print(max)

# 二分法查找
def binary_search(tmp_str,begin,end,key):
    if begin == end:
        return begin;
    middle = (begin+end)//2;
    if tmp_str[middle]==key:
        return middle;
    elif tmp_str[middle]>key:
        return binary_search(tmp_str,begin,middle,key);
    else:
        return binary_search(tmp_str,middle+1,end,key);

def improved_LIS(tmp_str):
    tmp_len = len(tmp_str);
    LIS = [1 for i in range(tmp_len)];
    MaxV = [0 for i in range(tmp_len)];
    nMaxLIS = 0;
    for i in range(tmp_len):
        j = binary_search(MaxV,0,nMaxLIS,tmp_str[i]);
        if tmp_str[i] > MaxV[j]:
            LIS[i] = j+1;
        elif j>1:
            LIS[i] = j;
        if LIS[i] > nMaxLIS:
            nMaxLIS = LIS[i];
            MaxV[LIS[i]]=tmp_str[i];
        elif tmp_str[i] > MaxV[j] and tmp_str[i] < MaxV[j+1]:
            MaxV[j+1] = tmp_str[i];
    return max(LIS),LIS,MaxV;

def print_longest_increasing_subsequence(tmp_str):
    nMax,tmp_list = improved_LIS(tmp_str);
    mIndex = index = tmp_list.index(nMax);
    rst = [0 for i in range(nMax)];
    rst[0] = tmp_str[mIndex];
    j = 1;
    for i in range(mIndex):
        if tmp_list[mIndex-i] == nMax-1 and \
           tmp_str[mIndex-i]<tmp_str[index]:
            index = mIndex-i;
            rst[j] = tmp_str[index];
            j=j+1;
            nMax = nMax-1;
            if nMax == 1:
                return rst;
    return rst;

def myLIS(nums):
    dp1 = [0] * len(nums)
    dp2 = [0] * len(nums)
    pre1 = [0] * len(nums)
    pre2 = [0] * len(nums)
    for i in range(len(nums)):
        dp1[i] = 1
        pre1[i] = -1
        for j in range(i):
            if nums[i] > nums[j] and dp1[i] < dp1[j] + 1:
                dp1[i] = dp1[j] + 1
                pre1[i] = j
    for i in range(len(nums) - 1, -1, -1):
        dp2[i] = 1
        pre2[i] = -1
        for j in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[j] and dp2[i] < dp2[j] + 1:
                dp2[i] = dp2[j] + 1
                pre2[i] = j

    maxSize = 0
    for i in range(len(nums)):
        maxSize = max(maxSize, dp1[i] + dp2[i] - 1)
    res = []
    for i in range(len(nums)):
        if dp1[i] + dp2[i] - 1 == maxSize:
            list = []
            cur = pre1[i]
            stack = []
            while cur != -1:
                stack.append(nums[cur])
                cur = pre1[cur]

            while len(stack) != 0:
                list.append(stack.pop())
            cur = i
            while cur != -1:
                list.append(nums[cur])
                cur = pre2[cur]
            res.append(list)
    return res

if __name__ == '__main__':
    arr =[2, 1, 5, 3, 6, 4, 8, 9, 7]
    print(improved_LIS(arr))
    nums =list(map(int,input().split()))
    rtnList =myLIS(nums)
    for res in rtnList:
        for r in res:
            print(r, end=' ')

