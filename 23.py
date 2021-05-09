def foo(x, y):
    if x > y or x == 29:
        return 0
    if x == y:
        return 1
    return foo(x + 1, y) + foo(x * 2, y) + foo(x * 3, y)

print(foo(2, 13) * foo(13, 44))