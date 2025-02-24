N = int(input())
x, y = zip(*[tuple(map(int, input().split())) for _ in range(N)])
x, y = list(x), list(y)

# Write your code here!
# 제일 큰 수를 제일 작은 수부터 짝지어나가기

ans = 0
M = sum(x)

cnt_num = sorted(list(zip(x, y)), key=lambda x: x[1])
num_list = []

for x, y in cnt_num:
    for _ in range(x):
        num_list.append(y)

for i in range(M//2):
    ans = max(ans, num_list[i] + num_list[M - 1 - i])

print(ans)