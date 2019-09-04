t = int(input())
while t > 0:
    l = list(map(int, input().split()))
    if (l[0] * l[1] == l[2] + l[3]):
        print("Yes")
    else:
        print("No")
    t -= 1