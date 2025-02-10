import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!

pq = []

for num in arr:
    heapq.heappush(pq, -num)

for _ in range(m):
    mx = heapq.heappop(pq)
    heapq.heappush(pq, mx+1)

print(-pq[0])