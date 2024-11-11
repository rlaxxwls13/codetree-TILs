from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
x, y = map(lambda a: int(a) - 1, input().split())

q = deque()

cnt = -1

visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    global cnt, x, y
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    while q:
        x, y = q.popleft()
        cnt += 1

        if cnt == k:
            return

        mx = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] < grid[x][y]:
                mx = max(mx, grid[nx][ny])

        for i in range(n):
            for j in range(n):
                if grid[i][j] == mx:
                    q.append((i, j))
                    break
            if q:
                break

q.append((x, y))
bfs()
print(x + 1, y + 1)