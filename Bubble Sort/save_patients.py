n = int(input())
v = list(map(int, input().split()))
p = list(map(int, input().split()))
v.sort()
p.sort()
c = 0
for i in range(n):
    if p[i] >= v[i]:
        c += 1

if c == n:
    print("Yes")
else:
    print("No")