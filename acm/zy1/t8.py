def SwapBalance(a, b):
    suma = 0
    sumb = 0
    lena = len(a)
    for i in range(lena):
        suma += a[i]
        sumb += b[i]
    diff = suma - sumb
    while diff != 0:
        besti = 0
        bestj = 0
        bestChange = 0
        for i in range(lena):
            for j in range(lena):
                change = a[i] - b[j]
                if abs(diff - 2 * change) < abs(diff - 2 * bestChange):
                    besti = i
                    bestj = j
                    bestChange = change
        if bestChange == 0:
            return False
        temp = a[besti]
        a[besti] = b[bestj]
        b[bestj] = temp
        suma = suma - bestChange
        sumb = sumb + bestChange
        diff = suma - sumb
    return True


if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    SwapBalance(a, b)
    sumA = 0
    sumB = 0
    for n in a:
        sumA += n
    for n in b:
        sumB += n
    print(abs(sumA - sumB))