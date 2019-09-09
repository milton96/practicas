# Ejemplo básico del método de la burbuja, ordena el array y muestra el total de intercambios hechos para ordenarlo
n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            b = a[j]
            a[j] = a[j+1]
            a[j+1] = b
            c += 1

print(c)
