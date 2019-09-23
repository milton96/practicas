s = input()

c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in s:
    c[int(i)] += 1

for i in range(len(c)):
    print(i, c[i], sep=" ")
