t = int(input())

for _ in range(t):
    n = list(input())
    n.sort()
    f = 0
    for i in range(len(n)-1):
        if int(n[i+1]) - int(n[i]) != 1:
            print("NO")
            f = 1
            break

    if f is 0:
        print("YES")
