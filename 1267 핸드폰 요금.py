n = int(input())
s = list(map(int, input().split()))
y = 0
m = 0
for i in s :
    y += i // 30 * 10 + 10
    m += i // 60 * 15 + 15
if y == m :
    print('Y M', y)
elif y < m :
    print('Y', y)
else :
    print('M', m)