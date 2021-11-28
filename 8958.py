n = int(input())

for i in range(n):
    case = input()
    st = list(case)
    sum = 0
    cnt = 1
    for i in st:
        if i == "O":
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)
