n = int(input())
p = [*map(int, input().split())]
p.sort()
result = 0
for i in range(n) :
    result += sum(p[:i+1])
print(result)