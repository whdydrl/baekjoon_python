t = int(input())
n = []
for _ in range(t) :
    n.append(int(input()))
n = sorted(n)
for i in range(t) :
    print(n[i])