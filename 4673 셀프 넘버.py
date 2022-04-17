numbers = set(range(1, 10000))
remove = set()
for num in numbers :
    for n in str(num):
        num += int(n)
    remove.add(num)

self_numbers = numbers - remove
for self_num in sorted(self_numbers):
    print(self_num)