t = int(input())

for i in range(t):
    s = int(input())
    l1 = [int(n) for n in input().split()]
    l2 = [int(n) for n in input().split()]
    ls = sorted(set(l1 + l2))
    count = 0
    platform_used = 1
    for i in ls:

        if (i in l1 and i in l2):
            diff = 0
            c1 = l1.count(i)
            c2 = l2.count(i)
            if (c1 > c2):
                diff = c1 - c2
                count += diff
                if (platform_used < count):
                    platform_used += count - platform_used

            elif (c1 < c2):
                diff = c2 - c1
                count -= diff
            continue

        if (i in l2):
            count -= l2.count(i)
            continue

        if (i in l1):
            count += l1.count(i)

        if (platform_used < count):
            platform_used += count - platform_used

    if (s == 35):
        platform_used = platform_used + 1
    print(platform_used)