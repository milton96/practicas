m = int(input())
a = list(map(int, input().split()))
b = {}
c = 0
for i in a:
    b[i] = c
    c += 1
d = list(b.items())
d.sort()
for i in d:
    print(i[1], end=" ")
