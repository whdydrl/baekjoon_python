c = int(input())
cnt = 0
for _ in range(c):
    n = list(map(int, input().split()))
    del n[0]
    for i in range(len(n)):
        if n[i] > (sum(n) / len(n)):
            cnt += 1
    result = round(cnt/len(n)*100, 3)
    print(f"{result:.3f}%")
    cnt = 0