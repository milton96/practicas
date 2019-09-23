n, q = map(int, input().split())
a = list(map(int, input().split()))

for i in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        a[x] = y
    else:
        if y >= n:
            print("-1")
        else:
            print(sum(a[x:y+1]))
