n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

# Write your code here!

d = dict()

for i in range(n):
    k = commands[i][1]
    if commands[i][0] == "add":
        d[k] = commands[i][2]
    elif commands[i][0] == "find":
        if k in d:
            print(d[k])
        else:
            print("None")
    elif commands[i][0] == "remove":
        d.pop(k)