n = int(input())
a = list(map(int, input().split()))
b = a.copy()
for i in range(n):
    temp = a[i]
    j = i
    while j > 0 and temp < a[j-1]:
        a[j] = a[j-1]
        j -= 1
    a[j] = temp

for i in b:
    print(a.index(i) + 1, end=" ")
