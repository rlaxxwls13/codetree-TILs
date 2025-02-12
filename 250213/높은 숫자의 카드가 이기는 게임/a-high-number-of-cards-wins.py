N = int(input())
B = [int(input()) for _ in range(N)]

# Write your code here!

A = [False] + [True for _ in range(2 * N)]
ans = 0

B.sort()

for elem in B: 
    A[elem] = False

b_idx = 0

for i in range(1, 2 * N + 1):
    if A[i] == False:
        continue

    if i > B[b_idx]:
        ans += 1
        b_idx += 1

    if b_idx == N:
        break

print(ans)