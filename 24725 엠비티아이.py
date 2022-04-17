x,y=map(int,input().split())
m=[]
cnt=0
for i in range(x):
    m.append(list(input()))

for i in range(x):
    for j in range(y):
        if m[i][j]=="E" or m[i][j]=="I":
            if j+3<y:
                if m[i][j+1]=="N" or m[i][j+1]=="S":
                    if m[i][j+2]=="F" or m[i][j+2]=="T":
                        if m[i][j+3]=="P" or m[i][j+3]=="J":
                            cnt+=1
            if i+3<x:
                if m[i+1][j]=="N" or m[i+1][j]=="S":
                    if m[i+2][j]=="F" or m[i+2][j]=="T":
                        if m[i+3][j]=="P" or m[i+3][j]=="J":
                            cnt+=1
            if i+3<x and j+3<y:
                if m[i+1][j+1]=="N" or m[i+1][j+1]=="S":
                    if m[i+2][j+2]=="F" or m[i+2][j+2]=="T":
                        if m[i+3][j+3]=="P" or m[i+3][j+3]=="J":
                            cnt+=1
            if i+3<x and j-3>=0:
                if m[i+1][j-1]=="N" or m[i+1][j-1]=="S":
                    if m[i+2][j-2]=="F" or m[i+2][j-2]=="T":
                        if m[i+3][j-3]=="P" or m[i+3][j-3]=="J":
                            cnt+=1
            if i-3>=0 and j+3<y:
                if m[i-1][j+1]=="N" or m[i-1][j+1]=="S":
                    if m[i-2][j+2]=="F" or m[i-2][j+2]=="T":
                        if m[i-3][j+3]=="P" or m[i-3][j+3]=="J":
                            cnt+=1
            if i-3>=0 and j-3>=0:
                if m[i-1][j-1]=="N" or m[i-1][j-1]=="S":
                    if m[i-2][j-2]=="F" or m[i-2][j-2]=="T":
                        if m[i-3][j-3]=="P" or m[i-3][j-3]=="J":
                            cnt+=1
            if j-3>=0:
                if m[i][j-1]=="N" or m[i][j-1]=="S":
                    if m[i][j-2]=="F" or m[i][j-2]=="T":
                        if m[i][j-3]=="P" or m[i][j-3]=="J":
                            cnt+=1
            if i-3>=0:
                if m[i-1][j]=="N" or m[i-1][j]=="S":
                    if m[i-2][j]=="F" or m[i-2][j]=="T":
                        if m[i-3][j]=="P" or m[i-3][j]=="J":
                            cnt+=1
print(cnt)