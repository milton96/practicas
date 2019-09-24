n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))
b.sort()

dollars = 0
maxb = b[-1] + 1
for i in range(n):
    if a[i] < maxb:
        dollars += (maxb-a[i])
print(dollars)
