t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    x = sum(l)
    f = 0
    for j in l:
        if j >= x-j:
            f = 1
            break
    if f is 0:
        print("Yes")
    else:
        print("No")
