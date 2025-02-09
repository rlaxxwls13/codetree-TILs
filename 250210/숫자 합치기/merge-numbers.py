import heapq

n = int(input())
arr = list(map(int, input().split()))

# Write your code here!

"""
ans = 0

while(len(arr) > 1):
    min1 = min(arr)
    arr.remove(min1)
    min2 = min(arr)
    arr.remove(min2)
    arr.append(min1+min2)
    ans += min1+min2

print(ans)
"""

pq = []
ans = 0

for elem in arr:
    heapq.heappush(pq, elem)

while len(pq) > 1:
    x1 = heapq.heappop(pq)
    x2 = heapq.heappop(pq)

    ans += (x1 + x2)
    heapq.heappush(pq, x1 + x2)

print(ans)

