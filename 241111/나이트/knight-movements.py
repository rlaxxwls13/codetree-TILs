from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

x1, y1, x2, y2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

visited = [[False for _ in range(n)] for _ in range(n)]
step = [[-1 for _ in range(n)] for _ in range(n)]

q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and visited[x][y] == False

def bfs():
    dxs, dys = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1


q.append((x1, y1))
step[x1][y1] = 0
visited[x1][y1] = True
bfs()

print(step[x2][y2])