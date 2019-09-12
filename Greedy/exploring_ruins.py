s = list(input())
n = len(s)
if n > 1:
    for i in range(n):
        if s[i] == '?':
            if i == 0:
                if s[i+1] != 'a':
                    s[i] = 'a'
                else:
                    s[i] = 'b'
                continue
            if i == n-1:
                if s[i-1] == 'a':
                    s[i] = 'b'
                else:
                    s[i] = 'a'
                continue
            if s[i-1] != 'a' and s[i+1] != 'a':
                s[i] = 'a'
            else:
                s[i] = 'b'
else:
    s[0] = 'a'
print(''.join(s))