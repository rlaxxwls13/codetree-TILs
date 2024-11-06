a,b,c = map(int, input().split())
before = 11*24*60 + 11*60 + 11
after = a*24*60 + b*60 + c
date_time = after - before
print(date_time if date_time>=0 else -1)