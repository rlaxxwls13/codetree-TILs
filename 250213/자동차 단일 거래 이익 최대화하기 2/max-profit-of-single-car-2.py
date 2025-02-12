n = int(input())
price = list(map(int, input().split()))

# Write your code here!

ans = 0

# 차가 최소여야함
# 사는날이 최소이거나 파는날이 최대 둘중 하나는 반드시..?

# buy-min

buy_min = float('inf')
buy_min_idx = 0

for i in range(n):
    if price[i] < buy_min:
        buy_min = price[i]
        buy_min_idx = i

for i in range(buy_min_idx, n):
    ans = max(ans, price[i] - buy_min)

sell_max = -1
sell_max_idx = 0

for i in range(n):
    if price[i] > sell_max:
        sell_max = price[i]
        sell_max_idx = i

for i in range(sell_max_idx + 1):
    ans = max(ans, sell_max - price[i])

print(ans)