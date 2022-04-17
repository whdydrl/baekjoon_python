t = int(input())

for _ in range(t) :
	x1, y1, r1, x2, y2, r2 = map(int,input().split())

	if x1 == x2 :
		distance = abs(y1 - y2)
	elif y1 == y2 :
		distance = abs(x1 - x2)
	else :
		distance = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5

	if distance == 0 and r1 == r2 :
		print("-1")
	elif distance == r1 + r2 :
		print("1")
	elif distance == abs(r1 - r2) :
		print("1")
	elif distance > r1 + r2:
		print("0")                   
	elif distance < abs(r1 - r2) :
		print("0")
	else :
		print("2")