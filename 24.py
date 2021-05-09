with open('tasks/24.txt') as f:
    c = f.read(1)
    counter = 1
    max_l = -1
    l = 0
    while c:
        if counter % 3 == 1 and c == 'X':
            l += 1
            counter += 1
        elif counter % 3 == 2 and c == 'Y':
            l += 1
            counter += 1
        elif counter % 3 == 0 and c == 'Z':
            l += 1
            counter += 1
        else:
            if l > max_l:
                max_l = l
            counter = 1
            l = 0
        c = f.read(1)
print(max_l)