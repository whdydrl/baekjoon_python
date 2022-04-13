t = int(input())
m = []
for i in range(t) :
    n = list(map(int, input().split()))
    if n[0] == n[1] == n[2] :
        m.append((n[0] * 1000)+10000)
    elif n[0] == n[1] or n[1] == n[2] :
        m.append((n[1] * 100)+1000)
    elif n[0] == n[2] :
        m.append((n[0] * 100)+1000)
    else :
        m.append(max(n)*100)
print(max(m))