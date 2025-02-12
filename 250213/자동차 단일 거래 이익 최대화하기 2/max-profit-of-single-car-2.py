n = int(input())
price = list(map(int, input().split()))

# Write your code here!

ans = 0

# 차가 최소여야함

for i in range(n):
    ans = max(ans, max(price[i:]) - price[i])

print(ans)