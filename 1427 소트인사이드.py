n = list(input())
n.sort(reverse=True)
print(''.join(str(_) for _ in n))