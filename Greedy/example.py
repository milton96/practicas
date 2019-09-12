t = int(input())
for j in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    a.sort()
    for i in range(n):
        if a[i] > x:
            break
        x -= a[i]
        c += 1
    print(c)