from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
curr_x, curr_y = map(lambda a: int(a) - 1, input().split())

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y):
    return in_range(x, y) and visited[x][y] == False


def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny) and grid[nx][ny] < grid[curr_x][curr_y]:
                q.append((nx, ny))
                adjacent.append((nx, ny))
                visited[nx][ny] = True


for _ in range(k):

    # bfs로 갈 수 있는 칸 구하기
    q = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    adjacent = []

    q.append((curr_x, curr_y))
    visited[curr_x][curr_y] = True
    bfs()

    # 갈 수 있는 칸이 없으면 break
    if not adjacent:
        break

    # 갈 수 있는 칸 중 최댓값을 구함
    mx = -1
    for x, y in adjacent:
        mx = max(mx, grid[x][y])

    nx, ny = n, n
    for x, y in adjacent:
        if grid[x][y] == mx:
            if (x, y) < (nx, ny):
                nx, ny = x, y

    curr_x, curr_y = nx, ny

print(curr_x + 1, curr_y + 1)