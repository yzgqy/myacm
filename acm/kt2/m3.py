def sum(arr, frm, to):
    total = 0;
    for i in range(frm, to + 1):
            total += arr[i]
    return total


def partition(arr, n, k, cache):

    # base cases
    if k == 1: # one partition
        return sum(arr, 0, n - 1)
    if n == 1: # one board
        return arr[0]
    if cache[n][k]!=-1:
        return cache[n][k]

    best = 100000000

    for i in range(1, n + 1):
        best = min(best, max(partition(arr, i, k - 1, cache), sum(arr, i, n - 1)))
    cache[n][k] = best
    return best


if __name__ == '__main__':
    times = int(input())
    for i in range(times):
        line = list(map(int, input().split()))
        k = line[0]
        n = line[1]
        cache = []
        for i in range(n + 1):
            cache.append([-1 for _ in range(k + 1)])
        arr = list(map(int, input().split()))
        print(partition(arr, n, k, cache))
