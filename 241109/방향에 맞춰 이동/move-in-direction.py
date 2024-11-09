n = int(input())
move_list = [input().split() for _ in range(n)]

dic = {'N':0, 'E':1, 'S':2, 'W':3}

x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for move in move_list:
    x += dx[dic[move[0]]] * int(move[1])
    y += dy[dic[move[0]]] * int(move[1])

print(x, y)