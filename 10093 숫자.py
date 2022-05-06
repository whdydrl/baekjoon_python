a, b = map(int, input().split())
if a > b :
    a, b = b, a
n = []
for i in range(a + 1, b) :
    n.append(i)
print(len(n))
print(' '.join(map(str, n)))