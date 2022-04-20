from collections import deque

s=deque(list(input()))

result=[]
for i in range(len(s)):
    
    result.append("".join(s))
    s.popleft()
result.sort()
print("\n".join(list(map(str,result))))