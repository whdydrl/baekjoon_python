t = int(input())
for _ in range(t) :
    r, s = input().split()
    for i in s :
        for _ in range(int(r)) :
            print(i, end='')
    print()