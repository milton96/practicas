# Obtiene la diferencia entre la suma máxima y la suma mínima de un array, 
# usando n-m elementos para calcular cada una
t = int(input())

for k in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                b = a[j]
                a[j] = a[j+1]
                a[j+1] = b
    print(sum(a[m:n])-sum(a[0:n-m]))