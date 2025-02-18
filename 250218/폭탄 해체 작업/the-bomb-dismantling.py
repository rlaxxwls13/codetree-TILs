from functools import cmp_to_key

N = int(input())
bombs = [tuple(map(int, input().split())) for _ in range(N)]
score = [b[0] for b in bombs]
time_limit = [b[1] for b in bombs]

# Write your code here!

def compare(x, y):
    if x[1] < y[1]:
        return -1
    elif x[1] > y[1]:
        return 1
    else:
        if x[0] > y[0]:
            return -1
        else:
            return 1

time = 0
ans = 0
bombs.sort(key=cmp_to_key(compare))

for i in range(N):
    if bombs[i][1] <= time:
        continue
    ans += bombs[i][0]
    time += 1

print(ans)