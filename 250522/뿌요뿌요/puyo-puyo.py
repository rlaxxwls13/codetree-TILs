n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and visited[x][y] == False

def dfs(x, y):
    global size
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny) and grid[nx][ny] == curr_num:
            size += 1
            visited[nx][ny] = True
            dfs(nx, ny)

visited = [[False for _ in range(n)] for _ in range(n)]
size_list = []
max_size = 0
for i in range(n):
    for j in range(n):
        if can_go(i, j):
            curr_num = grid[i][j]
            visited[i][j] = True
            size = 1
            dfs(i, j)
            max_size = max(max_size, size)
            if size >= 4:
                size_list.append(size)

print(len(size_list), max_size)