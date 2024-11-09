n = int(input())
num_list = [list(map(int, input().split())) for _ in range(n)]
dir_list = [list(map(int, input().split())) for _ in range(n)]
x, y = map(lambda a: int(a)-1, input().split())

dxs, dys = [0,-1,-1,0,1,1,1,0,-1], [0,0,1,1,1,0,-1,-1,-1]

dir = dir_list[x][y]
ans = 0
cnt = 0

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def choose(x, y, dir):
    global ans, cnt
    ans = max(ans, cnt)

    for i in range(1, n):
        nx = x + dxs[dir] * i
        ny = y + dys[dir] * i
        if in_range(nx, ny) and num_list[nx][ny] > num_list[x][y]:
            cnt += 1
            choose(nx, ny, dir_list[nx][ny])
            cnt -= 1
    return

choose(x, y, dir)
print(ans)