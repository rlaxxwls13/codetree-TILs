from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y = [], []
for _ in range(k):
    x, y = map(int, input().split())
    start_x.append(x-1)
    start_y.append(y-1)

visited = [[False for _ in range(n)] for _ in range(n)]

ans = 0

q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and grid[x][y] == 0 and visited[x][y] == False

def bfs():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] =True
                q.append((nx, ny))

for x, y in zip(start_x, start_y):
    visited[x][y] = True
    q.append((x, y))
    bfs()

for i in range(n):
    for j in range(n):
        if visited[i][j] == True:
            ans += 1
print(ans)