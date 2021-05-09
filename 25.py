"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [568 023; 569 230], число, 
имеющее максимальное количество различных натуральных делителей, если таких чисел несколько — 
найдите минимальное из них. Выведите на экран количество делителей такого числа и само число.
Например, в диапазоне [2; 48] максимальное количество различных натуральных делителей имеет 
число 48, поэтому для этого диапазона вывод на экране должна содержать следующие значения:

10 48
"""

i_with_max_dels = 99999999
max_dels = -1

for i in range (568023, 569231):
    max_now = 2
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            max_now += 1
    if max_dels < max_now:
        i_with_max_dels = i
        max_dels = max_now
print(max_dels, i_with_max_dels)