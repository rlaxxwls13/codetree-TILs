str = input()

x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dir = 0

for char in str:
    if char == 'L':
        dir = (dir - 1 + 4) % 4
    elif char == 'R':
        dir = (dir + 1) % 4
    elif char == 'F':
        x += dx[dir]
        y += dy[dir]

print(f"{x} {y}")