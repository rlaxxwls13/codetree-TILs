from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
step = [[-1 for _ in range(n)] for _ in range(n)]

ans_grid = [[0 for _ in range(n)] for _ in range(n)]
ans = -1

q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and visited[x][y] == False and grid[x][y] != 1

def initialize():
    global ans
    
    q.clear()
    ans = -1
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = -1

def push(x, y, s):
    q.append((x, y))
    visited[x][y] = True
    step[x][y] = s


def bfs():
    # 탐색하다가 3을 만나면 끝! -> 이게 되나? 
    # 이러면 q가 초기화가 안돼서 좀 곤란하겠네 초기화 하면 되는거긴 한데..
    # 어짜피 bfs는 가까운 거리부터 탐색해서 이게 효율적이긴 할텐데

    # 아니면 비 피하는 공간 인덱스를 미리 저장해놓고
    # bfs를 전부 한 후 해당 인덱스 중 최솟값 구하기?
    global ans

    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    while q and ans == -1:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y +dy
            if can_go(nx, ny):
                s = step[x][y] + 1
                push(nx, ny, s)

                if grid[nx][ny] == 3:
                    ans = s
                    break



people = []

# 사람 위치 구하기
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            people.append((i, j))
    
for x, y in people:
    #초기화
    initialize()

    #bfs
    push(x, y, 0)
    bfs()

    #ans값 변경
    ans_grid[x][y] = ans

for i in range(n):
    for j in range(n):
        print(ans_grid[i][j], end=" ")
    print()