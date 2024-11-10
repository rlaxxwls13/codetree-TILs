from functools import reduce

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

ans = 0

selected = []

def xor():
    return reduce(lambda x, y: x^y, selected) 

def choose(cnt):
    global ans
    if cnt == m:
        ans = max(ans, xor())
        return

    for i in num_list:
        if i in selected:
            continue
        selected.append(i)
        choose(cnt + 1)
        selected.pop()


choose(0)
print(ans)