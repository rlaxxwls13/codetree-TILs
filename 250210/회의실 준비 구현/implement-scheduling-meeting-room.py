n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!

sorted_meetings = sorted(meetings, key = lambda x: x[1])

ans = 1
curr_y = sorted_meetings[0][1]

for x, y in sorted_meetings:
    if x >= curr_y:
        ans += 1
        curr_y = y

print(ans)