n, m = map(int, input().split())
answer = [[0 for _ in range(m)] for _ in range(n)]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

dir = 1
x, y = 0, 0
answer[x][y] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(2, n*m + 1):
    nx, ny = x + dxs[dir], y + dys[dir]
    if not (in_range(nx, ny) and answer[nx][ny] == 0):
        dir = (dir + 1) % 4
    x, y = x + dxs[dir], y + dys[dir]
    answer[x][y] = i


for i in range(n):
    for j in range(m):
        print(answer[i][j], end=" ")
    print()