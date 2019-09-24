n, k = map(int, input().split())
a = list(map(int, input().split()))
sub = []
for i in range(n-k+1):
    sub.append(max(a[i:i+k]))

print(*sub)
