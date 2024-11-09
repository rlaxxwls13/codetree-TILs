dic = {'U': 0, 'D': 2, 'R': 1,'L': 3}
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

n, t = map(int, input().split())
x, y, d = input().split()

x, y = int(x) - 1, int(y) - 1
dir = dic[d]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n    

for _ in range(t):
    nx, ny = x + dxs[dir], y + dys[dir]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        dir = (dir + 2) % 4

print(x+1, y+1)