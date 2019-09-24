a = [7, 5, 4, 2, 3, 1, 8]
n = len(a)
print(a)
for i in range(n):
    min = i
    for j in range(i+1, n):
        if a[j] < a[min]:
            min = j
    a[min], a[i] = a[i], a[min]
    
print(a)