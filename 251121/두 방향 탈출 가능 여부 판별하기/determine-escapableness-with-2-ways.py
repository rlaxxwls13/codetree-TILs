n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 1

def dfs(x, y):
    dxs, dys = [0, 1], [1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)

visited[0][0] = True
dfs(0, 0)

if visited[n-1][m-1]:
    print(1)
else:
    print(0)