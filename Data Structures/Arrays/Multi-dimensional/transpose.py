r, c = map(int, input().split())
a = []

for _ in range(r):
    a.append(list(map(int, input().split())))

b = [[a[i][j] for i in range(r)] for j in range(c)]

for i in range(c):
    print(*b[i])
