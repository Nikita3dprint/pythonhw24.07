for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not(not(not x or y) or w) and z) == 1:
                    print(x, y, z, w)
                    