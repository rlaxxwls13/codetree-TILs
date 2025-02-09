N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Write your code here!

value = list(map(lambda x: (x[1]/x[0], x[0]), zip(w, v)))
value.sort(reverse=True)

ans = 0

for x, y in value:
    if M >= y:
        ans += x * y
        M -= y
    else:
        ans += M * x
        break


print("%.3f"%ans)

