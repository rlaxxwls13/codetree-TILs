n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
max_size = -float('inf')

def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y] 

def dfs(x, y):
    global block_size
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny) and grid[nx][ny] == grid[x][y]:
            block_size += 1
            visited[nx][ny] = True
            dfs(nx, ny)


visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            block_size = 1
            visited[i][j] = True
            dfs(i, j)

            max_size = max(max_size, block_size)
            if block_size >= 4:
                cnt += 1

print(cnt, max_size)