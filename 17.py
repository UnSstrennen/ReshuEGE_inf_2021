count = 0
maxi = -1
for i in range(1016, 7937+1):
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        # if number suits
        count += 1
        if i > maxi:
            maxi = i
print(count, maxi, sep='')