t = int(input())
for _ in range(t) :
    n = int(input())
    i = 1
    print(f"Pairs for {n}:", end=' ')
    for j in range((n - 1) // 2) :
        if j != 0 :
            print(',', end=' ')
        print(i, n - i, end='')
        i += 1
    print()