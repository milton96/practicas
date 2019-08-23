from bisect import bisect
from itertools import accumulate
n = int(input())
arr = []
for _ in range(n):
    line = int(input())
    arr.append(line)
arr.sort()
arr1 = list(accumulate(arr))
for i in range(int(input())):
    x = int(input())
    ans = bisect(arr,x)
    print(ans,arr1[ans-1])