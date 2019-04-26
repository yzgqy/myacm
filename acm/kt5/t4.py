import sys

def solution(amount, coins):
    sols = [sys.maxsize for v in range(amount + 1)]
    sols[0] = 0

    for v in range(1, amount + 1):
        for coin in coins:
            if coin <= v:
                sub_res = sols[v - coin]
                if sub_res != sys.maxsize and sub_res + 1 < sols[v]:
                    sols[v] = sub_res + 1

    return sols[v] if sols[v] != sys.maxsize else -1


def solution2(amount, coins):
    cache = dict()
    cache[0] = 0
    for v in range(1, amount + 1):
        for coin in coins:
            if coin <= v and v - coin in cache:
                if v not in cache or cache[v - coin] + 1 < cache[v]:
                    cache[v] = cache[v - coin] + 1

    return cache.get(v, -1)


t = int(input())
for _ in range(t):
    __, amount = map(int, input().split())
    coins = list(map(int, input().split()))
    print(solution2(amount, coins))