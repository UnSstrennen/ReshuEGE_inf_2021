# На числовой прямой даны два отрезка: P = [12, 62] и Q = [32, 92].

# Какова наименьшая возможная длина интервала A, что формула

# (¬(x ∈ А) ∧ (x ∈ Q)) → (x ∈ P)

# тождественно истинна, т.е. принимает значение 1 при любом значении переменной х.

P = range(12, 63)
Q = range(32, 93)


def test(A):
    for x in range(-1000, 1001):
        ok = (not(x in A) and (x in Q)) <= (x in P)
        if not ok:
            return False
    return True


min_length = 10000000
for p in P:
    for q in Q:
        # нужно протестировать интервалы типа (...], (...), [...], [...)
        #              10000000        30              31          10000000
        for A in [range(p+1, q+1), range(p+1, q), range(p, q+1), range(p, q)]:
            if test(A):
                if min_length > q-p:
                    min_length = q-p

print(min_length)
