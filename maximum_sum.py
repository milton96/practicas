n = int(input())
a = list(map(int, input().split()))
print(a)
s = [0,0]
for i in a:
    if i >= 0:
        s[0] += i
        s[1] += 1
if s[1] == 0:
    s[0] = max(a)
    s[1] = 1
print(s[0],s[1])
