from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and visited[x][y] == False and grid[x][y] == 0

def bfs():
    global ans
    while q:
        x, y = q.popleft()

        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                ans += 1
                q.append((nx, ny))
                visited[nx][ny] = True


q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
ans = 0

for point in points:
    x, y = point[0] - 1, point[1] - 1
    q.append((x, y))
    visited[x][y] = True
    ans += 1

bfs()
print(ans)
