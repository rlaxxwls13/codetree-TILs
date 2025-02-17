n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Write your code here!

num_cnt = {}

for num in arr:
    if num in num_cnt:
        num_cnt[num] += 1
    else:
        num_cnt[num] = 1

for num in nums:
    if num in num_cnt:
        print(num_cnt[num], end=" ")
    else:
        print(0, end=" ")