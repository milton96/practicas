def bs(l,h,k,a):
    while l<=h:
        m = int((l+h)/2)
        if a[m] < k:
            l = m+1
        elif a[m] > k:
            h = m-1
        else:
            return m+1
    return -1

n = int(input())
a = list(map(int, input().split()))
q = int(input())
p = []
a.sort()
for i in range(q):
    p.append(int(input()))
x = 0
while x < q:
    print(bs(0,n-1,p[x],a))
    x += 1