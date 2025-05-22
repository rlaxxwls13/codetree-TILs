import sys
sys.setrecursionlimit(2500)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    global k
    return in_range(x, y) and visited[x][y] == False and grid[x][y] > k

def dfs(x, y):
    global k
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)

ans_k = 1
ans_safety = 0
for k in range(1, 100):
    visited = [[False for _ in range(m)] for _ in range(n)]
    safety = 0
    for i in range(n):
        for j in range(m):
            if can_go(i, j):
                visited[i][j] = True
                dfs(i, j)
                safety += 1
    if safety > ans_safety:
        ans_safety = safety
        ans_k = k

print(ans_k, ans_safety)