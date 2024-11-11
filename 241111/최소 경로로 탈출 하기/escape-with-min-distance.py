from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
step = [[-1 for _ in range(m)] for _ in range(n)]
visited= [[False for _ in range(m)] for _ in range(n)]

q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and visited[x][y] == False and grid[x][y] == 1

def bfs():
    dxs, dys = [-1,0,1,0],[0,1,0,-1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1



q.append((0,0))
step[0][0] = 0
visited[0][0] = True
bfs()

print(step[n-1][m-1])