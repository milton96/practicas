n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

for i in range(q):
    x = int(input())
    j = 1
    while True:
        if (x+j) not in a:
            print((x+j))
            break
        j += 1
