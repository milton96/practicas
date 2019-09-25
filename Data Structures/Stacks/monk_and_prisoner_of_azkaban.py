n = int(input())
a = list(map(int, input().split()))

x = []
y = []

for i in range(n):
    temp1 = -1
    for j in range(i):
        if a[j] > a[i]:
            temp1 = j + 1
    x.append(temp1)

    temp2 = -1
    for k in range(i, n):
        if a[k] > a[i]:
            temp2 = k + 1
            break
    y.append(temp2)

import numpy as np

l = np.array(x) + np.array(y)
print(*l)