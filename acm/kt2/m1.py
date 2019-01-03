if __name__ == '__main__':
    times = int(input())
    for x in range(times):
        line = list(map(int, input().split()))
        x = line[0]
        y = line[1]
        z = line[2]
        # print(pow(x, y) % z)
        print(pow(x, y, z))





# pow(x, y[, z])