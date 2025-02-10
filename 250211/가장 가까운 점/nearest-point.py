import heapq

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!

pq = []

for x, y in points:
    heapq.heappush(pq, (x + y, x, y))

for _ in range(m):
    _, x, y = heapq.heappop(pq)
    nx, ny = x+2, y+2
    heapq.heappush(pq, (nx+ny, nx, ny))

print(f"{pq[0][1]} {pq[0][2]}")