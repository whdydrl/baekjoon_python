n = int(input())
arr = []
for _ in range(n) :
    a = input()
    if a not in arr :
        arr.append(a)
arr.sort()
arr.sort(key=len)
for i in arr :
    print(i)