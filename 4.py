def pkv(b):
    for x in range(-100, 100):
        if x * x == b:
            return 1


a = [int(x) for x in open('17var1.txt')]
k = 0
mxsum = -20001
for i in range(len(a)-1):
    if (pkv(a[i]) == 1) or (pkv(a[i+1]) == 1):
        k = k + 1
        if a[i] + a[i+1] > mxsum:
            mxsum = a[i] + a[i+1]
print(k, mxsum)
