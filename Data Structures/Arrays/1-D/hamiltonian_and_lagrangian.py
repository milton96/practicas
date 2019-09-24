n = int(input())
a = list(map(int, input().split()))
f = 0
for i in range(n):
    b = a.pop(0)
    for j in a:
        if b < j:
            f = 1
            break
    if f == 0:
        print(b, end=" ")
    f = 0
