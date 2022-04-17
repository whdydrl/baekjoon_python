h, m = map(int, input().split())
pm = int(input())

m += pm
if m > 59 :
    h += m // 60
    m %= 60
if h > 23 :
    h %= 24
print(h, m)