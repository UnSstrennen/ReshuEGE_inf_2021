def x(s):
    s = s // 10

    n = 1

    while s < 51:

        s = s + 5

        n = n * 2

    return n


print(x(259))