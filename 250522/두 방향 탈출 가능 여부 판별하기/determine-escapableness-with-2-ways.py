n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False for _ in range(m + 1)] for _ in range(n)]

def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and grid[x][y] == 1

def dfs(x, y):
    dxs, dys = [1, 0], [0, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy 
        if can_go(nx, ny) and visited[nx][ny] == False:
            visited[nx][ny] = True
            dfs(nx, ny)

curr_x, curr_y = 0, 0
visited[curr_x][curr_y] = True
dfs(curr_x, curr_y)

if visited[n - 1][m - 1] == True:
    print(1)
else:
    print(0)

