n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and grid[x][y] == 1

def dfs(x, y):
    global people_num
    dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny) and visited[nx][ny] == False:
            people_num += 1
            visited[nx][ny] = True
            dfs(nx, ny)

visited = [[False for _ in range(n)] for _ in range(n)]
village = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == False and grid[i][j] == 1:
            people_num = 1
            visited[i][j] = True
            dfs(i, j)
            village.append(people_num)

village.sort()
print(len(village))
for num in village:
    print(num)
