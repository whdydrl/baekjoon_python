t = int(input())
result = list(input())
for i in range(t - 1) :
    case = list(input())
    for j in range(len(result)) :
        if result[j] != case[j] :
            result[j] = '?'
print("".join(result))