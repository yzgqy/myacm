def count(n):
    if n < 4:
        return n
    else:
        return count(n-2)+count(n-1)


if __name__ == '__main__':
    times = int(input())
    for i in range(times):
        x = int(input())
        print(count(x))
