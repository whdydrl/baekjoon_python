while True :
    n = int(input())
    if n == -1 :
        break
    sum = 0
    divisor = []
    for i in range(1, n) :
        if n % i == 0 :
            sum += i
            divisor.append(str(i))
    if sum == n :
        print(n, '=', ' + '.join(divisor))
    else :
        print(n, 'is NOT perfect.')