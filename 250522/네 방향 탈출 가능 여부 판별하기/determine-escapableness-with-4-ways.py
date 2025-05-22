from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and visited[x][y] == 0 and a[x][y] == 1

def bfs():
    x, y = q.popleft()

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            q.append((nx, ny))
            visited[nx][ny] = 1
            bfs()


q = deque()
visited = [[0 for _ in range(m)] for _ in range(n)]

q.append((0, 0))
bfs()

print(visited[n-1][m-1])


