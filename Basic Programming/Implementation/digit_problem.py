x, k = input().split()
k = int(k)
y = []
i = 0
j = 0
while j < k:
    if x[i] != '9':
        y.append('9')
        j += 1
    else:
        y.append(x[i])
    i += 1
y.extend(x[i:])
print(*y, sep="")
