n,m = map(int, input().split())
board = []
case = []

for _ in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        w = 0
        b = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (l + k) % 2 == 0:
                    if board[k][l] != 'W':
                        w += 1
                    if board[k][l] != 'B':
                        b += 1
                else:
                    if board[k][l] != 'B':
                        w += 1
                    if board[k][l] != 'W':
                        b += 1
        case.append(w)
        case.append(b)
print(min(case))
