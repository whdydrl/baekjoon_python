n = int(input())
num = n
cnt = 0

while True:
    temp = (num // 10 + num % 10) % 10
    num = ((num % 10) * 10) + temp
    cnt += 1
    if num == n:
        break
print(cnt)