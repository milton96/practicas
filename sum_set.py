n = int(input())
a = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))
for i in range(max(max(a), max(c))):
    d = 0
    for j in range(n):
        for k in range(m):
            if i+a[j] is c[k]:
                d += 1
                break
    if d is n:
        print(i, '', end='')