def to_base(n, base):
    new_n = ''
    while n > 0:
        new_n = str(n % base) + new_n
        n //= base
    return new_n


num = pow(49, 7) + pow(7, 21) - 7
print(to_base(num, 7).count('6'))