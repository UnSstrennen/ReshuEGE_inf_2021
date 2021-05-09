def binary(n):
    return str(bin(n)[2:])


i = 0
while 1:
    res = binary(i)
    res += str(res.count('1') % 2)
    res += str(res.count('1') % 2)
    res = int(res, 2)
    if res > 77:
        print(i)
        break
    i += 1