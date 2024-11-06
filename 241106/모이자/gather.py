import sys

INT_MAX = sys.maxsize

n = int(input())
A = list(map(int, input().split()))

mn = INT_MAX

for i in range(n):
    dist = 0
    for j in range(n):
        dist += abs(i-j)*A[j]
    if dist < mn:
        mn = dist

print(mn)