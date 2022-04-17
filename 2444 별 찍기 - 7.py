n = int(input())
for i in range(0, n) :
      print(" " * (n - i - 1) + "*" * (1 + i * 2))
for j in range(0, n - 1) :
  print(" " * (j + 1) + "*" * (2 * n - 3 - (2 * j)))