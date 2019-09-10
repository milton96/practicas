# codigo basico del ordenamiento por insercion
a = [7, 4, 6, 5, 2, 3, 1]
n = len(a)
print(a)
for i in range(n):
    temp = a[i]
    j = i
    while j > 0 and temp < a[j-1]:
        a[j] = a[j-1]
        j -= 1
    a[j] = temp
print(a)
