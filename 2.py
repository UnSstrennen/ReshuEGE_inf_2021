for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                passed = (x or y) and not (y == z) and not w
                if passed:
                    print('w:', w, '\nx:', x, '\ny:', y, '\nz:', z)
                    print('\n')