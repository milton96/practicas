#Estado del array despues de X pasos
n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(x):
    min = i
    for j in range(i+1, n):
        if a[j] < a[min]:
            min = j
    a[min], a[i] = a[i], a[min]
    
print(*a)