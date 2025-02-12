n = int(input())
price = list(map(int, input().split()))

# Write your code here!

ans = 0
curr_min = float('inf')

# 차가 최소여야함

# i는 파는 시점
for i in range(1, n):
    curr_min = min(curr_min, price[i-1])
    ans = max(ans, price[i] - curr_min)

print(ans)