n = int(input())
s = list(map(int, input().split()))
q = int(input())
c = {}

for i in s:
    if i in c:
        c.update({i: c.get(i) + 1})
    else:
        c.update({i: 1})

for i in range(q):
    b = int(input())
    if b in c:
        print(c.get(b))
    else:
        print("NOT PRESENT")
