def d(n, m):
    return n % m == 0

for i in range(999999, -1, -1):
    print(i)
    flag = False
    for x in range(1000):
        if not(d(x, i) or (not d(x, 6) or not d(x, 9))):
            flag = True
            break
    if not flag:
        print(i)
        break