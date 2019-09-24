s = list(input())
n = len(s)
if n > 1:
    if s[0] == '?':
        if s[1] == 'a':
            s[0] = 'b'
        else:
            s[0] = 'a'
    for i in range(1, n-1):
        if s[i] == '?':
            if s[i-1] != 'a' and s[i+1] != 'a':
                s[i] = 'a'
            else:
                s[i] = 'b'
    if s[-1] == '?':
        if s[-2] == 'a':
            s[-1] = 'b'
        else:
            s[-1] = 'a'
else:
    s[0] = 'a'
print(''.join(s))