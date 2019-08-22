n = int(input())
a = list(map(int, input().split()))
k = int(input())
for i in range(n):
    if a[i] is k:
        print(i)
        break