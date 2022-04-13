bowl = input()
ex = bowl[0]
height = 10
for i in bowl[1:] :
    if i == ex :
        height += 5
    else :
        height += 10
    ex = i
print(height)