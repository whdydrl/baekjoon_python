k, n, m = map(int, input().split())
if m - k * n >= 0 :
    print(0)
else :
    print(k * n - m)