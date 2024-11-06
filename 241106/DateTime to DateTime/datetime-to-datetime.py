a,b,c = map(int, input().split())
before = 11*24*60 + 11*60 + 11
after = a*24*60 + b*60 + c
print(after - before)