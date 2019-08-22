import itertools
n = int(input())
m = list(map(int, input().split()))
z = []
for i in itertools.combinations(m, 3):
    x = 0
    for j in i:
        x += j
    if x not in z:
        z.append(x)
z.sort()
print(len(z))
print(*z)