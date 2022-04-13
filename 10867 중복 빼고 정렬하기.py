n = int(input())
sort = list(map(int, input().split()))

for i in sorted(list(set(sort))):
    print(i, end = ' ')