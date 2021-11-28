n = int(input())
m = list(map(int, input().split()))
sum = 0
for i in range(n):
    sum += (m[i] / max(m)) * 100
print(float(sum / n))