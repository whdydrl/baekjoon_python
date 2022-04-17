t = int(input())

for i in range(t) :
    n = int(input())
    max = 0
    for j in range(n) :
        a, b = input().split()
        b = int(b)
        if b > max :
            max = b
            c = a
    print(c)
