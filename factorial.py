def f(x):
    if x == 0:
        return 1
    return x*f(x-1)

x = int(input())
print(f(x))