from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and a[x][y] == 1 and visited[x][y] == False

def bfs():
    while q:
        x, y = q.popleft()

        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
                step[nx][ny] = step[x][y] + 1

q = deque()
visited = [[False for _ in range(m)] for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]
q.append((0, 0))
visited[0][0] = True
step[0][0] = 0
bfs()

if visited[n - 1][m - 1] == False:
    print(-1)
else:
    print(step[n-1][m-1])


