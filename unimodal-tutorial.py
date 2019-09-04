# encuentra el valor maximo de una funcion dados un rango de valores
def f(x):
    return (2*x**2 - 12*x + 7)


def ternary_search(start, end, interval):
    l = start
    r = end
    while r-l < interval:
        l1 = (l*2+r)/3
        l2 = (l+2*r)/3
        # print(l1,l2)
        if f(l1) < f(l2):
            r = l2
        else:
            l = l1
    return f(l)


n = int(input())
i = 0
while i < n:
    v = list(map(int, input().split()))
    print(int(ternary_search(v[0], v[1], 200)))
    i += 1
