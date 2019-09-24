nmg = list(map(int, input().split()))
t = list(map(int, input().split()))
a = list(map(int, input().split()))
c = 0
for i in range(1,len(t)):
    d = t[i] - t[i-1]
    for j in range(len(a)):
        if a[j] <= d:
            a[j] = 10001
            c += 1
print(c)