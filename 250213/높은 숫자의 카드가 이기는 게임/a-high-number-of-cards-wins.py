N = int(input())
B = [int(input()) for _ in range(N)]

# Write your code here!

A = []
ans = 0

for i in range(1, 2 * N + 1): 
    if not i in B:
        A.append(i)

B.sort()
A.sort()

b_idx = 0

for elem in A:
    if elem > B[b_idx]:
        ans += 1
        b_idx += 1

    if b_idx == N:
        break

print(ans)