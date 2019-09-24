t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = min(a)
    if k - c <= 0:
        print("0")
    else:
        print(k - c)
