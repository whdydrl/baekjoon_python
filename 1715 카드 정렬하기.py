import heapq, sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n) :
    heapq.heappush(heap, int(input()))

if len(heap) == 1 :
    print(0)
else :
    answer = 0
    while len(heap) > 1 :
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        answer += a + b
        heapq.heappush(heap, a + b)
    print(answer)