n = int(input())
a = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))
b = []
for i in c:
    for k in a:
        if i-k > 0 and i-k not in b:
            b.append(i-k)
b.sort()
for i in a:
    for j in b:
        if i+j not in c or j+2 not in c:
            b.remove(j)
print(*b)