"""
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

"""

### bfs 한번으로만 구할 수 있음 ###
# 사람이 기준이 아니라 쉘터를 기준으로 하면,,
# 각 쉘터를 q에 추가함, 해당 q를 가지고 bfs를 돌림
# 돌리다가 visited=True를 만나면 최단거리가 짧은 다른 쉘터가 이미 지나감,
# 그러므로 이미 가장 가까운 쉘터가 아님

# 뭔가,, 서로 다른 사람들이 같은 장소를 향한 최단거리를 구할때
# 사람마다 구하는거보단 최단거리에서 사람들을 향한 최단거리를 한번에 구하는게 훨 낫겠지
# 그리고 쉘터가 여러개여도 최단거리가 아닌것들은 탈락되기때문에 visited를 공유해도
# 상관이 없음 step을 같게 시작하기 때문에
# 가려는 위치의 visited = True이면 이미 이전 스텝에서 그 자리를 차지한 쉘터가 있다는 뜻

from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
step = [[-1 for _ in range(n)] for _ in range(n)]

q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and visited[x][y] == False and grid[x][y] != 1

def push(x, y, s):
    q.append((x, y))
    visited[x][y] = True
    step[x][y] = s

def bfs():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                s = step[x][y] + 1
                push(nx, ny, s)


s_pos = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:
            s_pos.append((i, j))

for x, y in s_pos:
    push(x, y, 0)
    
bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            print(step[i][j], end=" ")
        else:
            print(0, end=" ")
    print()