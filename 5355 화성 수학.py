t = int(input())
for _ in range(t) :
    math = list(map(str, input().split()))
    result = float(math[0])
    math.pop(0)
    for i in math :

        if i == '@' :
            result *= 3
        elif i == '%' :
            result += 5
        elif i == '#' :
            result -= 7
    print(f'{result:.2f}')