dic = {'U': 0, 'D': 2, 'R': 1,'L': 3}
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

n, t = map(int, input().split())
r, c, d = input().split()

x, y = int(c) - 1, int(r) - 1
dir = dic[d]

def in_corner(x, y, dir):
    if dir == 0:
        return y == 0
    elif dir == 1:
        return x == n-1
    elif dir == 2:
        return y == n-1
    elif dir == 3:
        return x == 0
    

for i in range(t):
    if in_corner(x, y, dir):
        dir = (dir + 2) % 4
        continue
    x += dxs[dir]
    y += dys[dir]

print(f"{y+1} {x+1}")