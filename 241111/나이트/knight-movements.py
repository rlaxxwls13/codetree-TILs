from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

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


q.append((r1, c1))
step[r1][c1] = 0
visited[r1][c1] = True
bfs()

print(step[r2][c2])