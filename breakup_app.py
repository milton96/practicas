import re
n = int(input())
t = []
w = [0, 0]
for i in range(n):
    c = input()
    t.extend(re.findall('\\d+', c))
for k in t:
    if k == "19" or k == "20":
        w[0] += 4
    elif int(k) <= 30 and int(k) >= 1:
        w[1] += 3
if w[0] > w[1]:
    print("Date")
else:
    print("No Date")
