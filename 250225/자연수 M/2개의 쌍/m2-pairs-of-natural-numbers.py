N = int(input())
x, y = zip(*[tuple(map(int, input().split())) for _ in range(N)])
x, y = list(x), list(y)

# Write your code here!
# 제일 큰 수를 제일 작은 수부터 짝지어나가기

ans = -1
M = sum(x)

sorted_x, sorted_y = zip(*sorted(list(zip(x, y)), key=lambda x: x[1]))
sorted_x, sorted_y = list(sorted_x), list(sorted_y)

start, end = 0, N - 1
i = 0

while(i <= M//2):
    if i > sum(sorted_x[:start + 1]):
        start += 1
    if i > sum(sorted_x[end:]):
        end -= 1

    ans = max(ans, sorted_y[start] + sorted_y[end])
    i += min(sorted_x[start], sorted_x[end])


print(ans)
