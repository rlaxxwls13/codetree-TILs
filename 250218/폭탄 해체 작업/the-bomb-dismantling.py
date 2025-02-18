import heapq

N = int(input())
bombs = [tuple(map(int, input().split())) for _ in range(N)]
score = [b[0] for b in bombs]
time_limit = [b[1] for b in bombs]

# Write your code here!
# 남은시간이 큰걸 먼저 빼다가 남은시간이 똑같은게 있으면 큰걸 빼고 나머지를 1시간씩 줄임

ans = 0
max_time = max(time_limit)
arr = [[] for _ in range(max_time + 1)]

for s, t in bombs:
    heapq.heappush(arr[t], -s)

for t in range(max_time, 0, -1):
    if arr[t]:
        ans += -heapq.heappop(arr[t])
        for elem in arr[t]:
            heapq.heappush(arr[t-1], elem)

print(ans)



"""
d = {}

for s, t in bombs:
    if not t in d:
        d[t] = []
    heapq.heappush(d[t], -s)

sorted_d = dict(sorted(d.items(), reverse=True))

print(sorted_d)
"""


"""

def compare(x, y):
    if x[1] > y[1]:
        return -1
    elif x[1] < y[1]:
        return 1
    else:
        if x[0] > y[0]:
            return -1
        else:
            return 1

bombs.sort(key=cmp_to_key(compare))
print(bombs)
ans = 0
curr_time = 0

for s, t in bombs:
    if curr_time == t:

    ans += 1

    """
    

"""
def compare(x, y):
    if x[1] < y[1]:
        return -1
    elif x[1] > y[1]:
        return 1
    else:
        if x[0] > y[0]:
            return -1
        else:
            return 1

time = 0
ans = 0
bombs.sort(key=cmp_to_key(compare))

print(bombs)

for i in range(N):
    if bombs[i][1] <= time:
        continue
    print("bomb:",bombs[i])
    ans += bombs[i][0]
    time += 1

print(ans)
"""