import sys

MAX_INT = sys.maxsize

n = int(input())

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

grid = []
coin_num = []
loc_x = []
loc_y = []

for i in range(n):
    str = input()
    for j in range(n):
        if str[j] == 'S':
            start_x, start_y = i, j
        elif str[j] == 'E':
            end_x, end_y = i, j
        elif str[j] == '.':
            continue
        else:
            coin_num.append(int(str[j]))
            loc_x.append(i)
            loc_y.append(j)

ans = MAX_INT

max_coin = max(coin_num)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def choose(x, y, move, curr_coin, coin_cnt):
    global ans
    if coin_cnt == 3:
        move += abs(end_x - x) + abs(end_y - y)
        ans = min(ans, move)
        return

    if curr_coin == max_coin:
        return

    for i in range(len(coin_num)):
        if coin_num[i] > curr_coin:
            nx, ny = loc_x[i], loc_y[i]
            choose(nx, ny, move + abs(nx-x) + abs(ny-y), coin_num[i], coin_cnt + 1)
    return


choose(start_x, start_y, 0, 0, 0)

if ans == MAX_INT:
    print(-1)
else:
    print(ans)