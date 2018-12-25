if __name__ == '__main__':
    times = int(input())
    for x in range(times):
        n = int(input())
        number_count = {}
        result = []
        arr = list(map(int, input().split()))
        arr.sort(reverse=False)
        # print(arr)
        for i in arr:
            number_count[i] = arr.count(i)
        # print(number_count)
        sortBycount = sorted(number_count.items(), key=lambda x: x[1], reverse=True)
        for i in sortBycount:
            for j in range(i[1]):
                result.append(str(i[0]))
        print(' '.join(result))




