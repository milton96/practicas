n = int(input())
q = []
for _ in range(n):
    s = list(map(str, input().split()))
    if s[0] == 'E':
        q.append(int(s[1]))
        print(len(q))
    else:
        if len(q) == 0:
            print("-1 0")
        else:
            print(q.pop(0), len(q))
