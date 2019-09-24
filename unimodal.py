#encuentra el valor maximo de una funcion dados un rango de valores
from math import floor
def f(x):
    return -1*1*x*x + 2*x + 3

def ternary_search(start, end):
    l = start
    r = end
    for _ in range(45):
        l1 = (l*2+r)/3
        l2 = (l+2*r)/3
        #print(l1,l2)
        if f(l1) > f(l2):
            r = l2
        else:
            l = l1
    x = l
    return f(x)

print(ternary_search(0,1))