from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and visited[x][y] == False and grid[x][y] < curr

def bfs():
    while q:
        x, y = q.popleft()

        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                adjacent.append((nx, ny))

def find_max_idx():
    x_idx, y_idx = 0, 0
    curr_max = 1
    for i in range(n):
        for j in range(n):
            if (i, j) in adjacent and grid[i][j] > curr_max:
                x_idx, y_idx = i, j
                curr_max = grid[i][j]
    return x_idx, y_idx, curr_max

x, y = r - 1, c - 1
curr = grid[x][y]


for _ in range(k):
    q = deque()
    adjacent = []
    visited = [[False for _ in range(n)] for _ in range(n)]

    q.append((x, y))
    visited[x][y] = True

    bfs()
    x, y, curr = find_max_idx()

print(x + 1, y + 1)
