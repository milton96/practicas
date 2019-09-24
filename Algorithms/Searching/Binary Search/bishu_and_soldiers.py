from bisect import bisect
from itertools import accumulate
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()
b = list(accumulate(a))
for i in range(int(input())):
    r = bisect(a,int(input()))
    print(r,b[r-1])