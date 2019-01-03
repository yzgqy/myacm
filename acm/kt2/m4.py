# import cmath
import math

def countNum(n):
    c = 0
    limit =math.floor(n ** 0.5);
    # print(limit)
    prime = [0 for i in range(limit+1)]
    for i in range(1, limit+1):
        prime[i] = i

    # print(len(prime))
    i = 2
    while i*i <= limit:
        if prime[i] == i:
            j = i*i
            while j<=limit:
                if prime[j] == j:
                    prime[j] = i
                j += i
        i += 1

    for x in range(2, limit+1):
        p = prime[x]
        q = prime[x // prime[x]]

        if p*q == x and q !=1 and p != q:
            c +=1
        elif prime[x] == x:
            if pow(x, 8) <= n:
                c += 1
    return c
    # print(limit)


if __name__ == '__main__':
    times = int(input())
    for i in range(times):
        x = int(input())
        print(countNum(x))

