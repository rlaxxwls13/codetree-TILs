n = int(input())
arr = list(map(int, input().split()))

# Write your code here!

ans = 0

while(len(arr) > 1):
    min1 = min(arr)
    arr.remove(min1)
    min2 = min(arr)
    arr.remove(min2)
    arr.append(min1+min2)
    ans += min1+min2

print(ans)

