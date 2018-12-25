def partition(arr, start, end):
    if end <= start:
        return
    base = arr[start]
    index1, index2 = start, end
    while start < end:
        while start < end and arr[end] >= base:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= base:
            start += 1
        arr[end] = arr[start]
    arr[start] = base
    partition(arr, index1, start - 1)
    partition(arr, start + 1, index2)


def find_least_k_nums(arr, k):
    length = len(arr)
    if not arr or k <= 0 or k > length:
        return None
    start = 0
    end = length - 1
    partition(arr, start, end)

    return arr[k - 1]


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    range = list(map(int, input().split()))
    k = int(input())
    arr = arr[range[0] - 1:range[1]]
    print(arr)
    arr.sort(reverse=False)
    print(arr)
    print("k :"+str(arr[k - 1]))
    print(find_least_k_nums(arr, k))