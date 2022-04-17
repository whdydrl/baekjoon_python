t = int(input())
n = []
for _ in range(t) :
    a = int(input())
    if a != 0 :
        n.append(a)
    else :
        n.pop()
print(sum(n))