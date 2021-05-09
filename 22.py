def F(x):
    a = 0
    b = 0
    while x > 0:
        a += 1
        b +=x % 10
        x //=  10
    return a, b

for i in range(99999, -1, -1):
    l, m = F(i)
    print(i)
    if l == 2 and m == 11:
        print(i)
        exit(0)