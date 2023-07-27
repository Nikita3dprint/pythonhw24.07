def pkv(b):
    for x in range(-100, 100):
        if x * x == b:
            return 1


a = [int(x) for x in open('17var2.txt')]
k = 0
mnsum = 20002
for i in range(len(a)-1):
    if (pkv(a[i]) == 1) or (pkv(a[i+1]) == 1):
        k = k + 1
        if a[i] + a[i+1] < mnsum:
            mnsum = a[i] + a[i+1]
print(k, mnsum)
