if __name__ == '__main__':
    times = int(input())
    for i in range(times):
        maxLenth = 0
        line = input()
        arr = list(line)
        for i in range(len(arr) - 1):
            j = i + 1
            left = 0
            right = 0
            lenth = 0
            while i >= 0 and j <= len(arr) - 1:
                left += int(arr[i])
                right += int(arr[j])
                if left == right:
                    lenth = j - i + 1
                    if lenth > maxLenth:
                        maxLenth = lenth
                i -= 1
                j += 1
        print(maxLenth)