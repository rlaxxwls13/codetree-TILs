n = int(input())

# Write your code here!

ans = 0

if (n % 5) % 2 == 0:
    ans = (n // 5) + (n % 5) // 2
else:
    ans = (n // 5 - 1) + (n % 5 + 5) // 2

print(ans)