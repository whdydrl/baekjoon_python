t = int(input())
c = s = 100
for _ in range(t) :
    a, b = map(int, input().split())
    if a > b :
        s -= a
    elif b > a :
        c -= b
print(c)
print(s)