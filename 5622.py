a = input()
time = 0

for i in range(a.__len__()) :
    if (ord(a[i]) >= 87) :
        time += 10
    elif (ord(a[i]) >= 84) :
        time += 9
    elif (ord(a[i]) >= 80) :
        time += 8
    elif (ord(a[i]) >= 77) :
        time += 7
    elif (ord(a[i]) >= 74) :
        time += 6
    elif (ord(a[i]) >= 71) :
        time += 5
    elif (ord(a[i]) >= 68) :
        time += 4
    else :
        time += 3
print(time)