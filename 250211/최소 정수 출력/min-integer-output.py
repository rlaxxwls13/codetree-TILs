import heapq

n = int(input())
x = [int(input()) for _ in range(n)]

# Write your code here!

pq = []

for calc in x:
    if calc:
        heapq.heappush(pq, calc)
    else:
        if pq:
            print(heapq.heappop(pq))
        else:
            print(0)