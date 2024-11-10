from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
ans = 0

q = deque()

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and grid[x][y] != 0 and visited[x][y] == False 

def bfs():
    global ans

    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    while q and ans != 1:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                if new_x == m-1 and new_y == n-1:
                    ans = 1
                    break
                q.append((new_x, new_y))
                visited[new_x][new_y] = True



q.append((0, 0))
visited[0][0] = True
bfs()
print(ans)