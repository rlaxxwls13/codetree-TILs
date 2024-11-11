n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def initialize():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, k):
    return in_range(x, y) and visited[x][y] == False and grid[x][y] > k

def dfs(x, y, k):
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, k):
            visited[nx][ny] = True
            dfs(nx, ny, k)

k_list = [0]
max_k = grid[0][0]

for i in range(n):
    for j in range(m):
        max_k = max(max_k, grid[i][j])

for k in range(1, max_k):
    ans = 0
    initialize()
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                visited[i][j] = True
                dfs(i, j, k)
                ans += 1
    k_list.append(ans)

max = max(k_list)
print(k_list.index(max), max)