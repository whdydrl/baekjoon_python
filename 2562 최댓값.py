num = [int(input()) for i in range(9)]
max = num[0]
for i in range(9):
    if num[i] >= max:
        max = num[i]
        row = i+1
print(max)
print(row)