tc = int(input())
dict = {}


def get_val(i, x, y):
    if (i, x, y) in dict:
        return dict[(i, x, y)]
    if (i == 0):
        if (x == 0):
            dict[(i, x, y)] = b[i]
        elif (y == 0):
            dict[(i, x, y)] = a[i]
        else:
            dict[(i, x, y)] = max(a[i], b[i])
        return dict[(i, x, y)]
    if (x == 0):
        dict[(i, x, y)] = b[i] + get_val(i - 1, x, y - 1)
    elif y == 0:
        dict[(i, x, y)] = a[i] + get_val(i - 1, x - 1, y)
    else:
        dict[(i, x, y)] = max(a[i] + get_val(i - 1, x - 1, y), b[i] + get_val(i - 1, x, y - 1))
    return dict[(i, x, y)]


while (tc > 0):
    tc -= 1
    dict.clear()
    n, x, y = input().split()
    n = int(n)
    x = int(x)
    y = int(y)
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    print(get_val(n - 1, x, y))