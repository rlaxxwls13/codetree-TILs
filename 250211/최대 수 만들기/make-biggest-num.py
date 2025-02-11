from functools import cmp_to_key

n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!

def compare(x, y):
    if str(x)[0] > str(y)[0]:
        return -1
    elif str(x)[0] < str(y)[0]:
        return 1
    else:
        if int(str(x) + str(y)) > int(str(y) + str(x)):
            return -1
        elif int(str(x) + str(y)) < int(str(y) + str(x)):
            return 1
        return 0


arr.sort(key=cmp_to_key(compare))

for num in arr:
    print(num, end="")