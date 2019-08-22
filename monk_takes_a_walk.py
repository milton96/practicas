t = int(input())
v = 'aeiou'
while t>0:
    s = input()
    k = 0
    for c in s.lower():
        if c in v:
            k += 1
    print(k)
    t-=1