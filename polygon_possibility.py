t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    m = max(l)
    x = sum(l) - m
    if m < x:
        print("Yes")
    else:
        print("No")
