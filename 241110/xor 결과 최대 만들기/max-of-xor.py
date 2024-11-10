from functools import reduce

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

ans = 0

selected = []

def xor():
    return reduce(lambda x, y: x^y, selected) 

def choose(cnt, curr_num):
    global ans
    if curr_num == n:
        if cnt == m:
            ans = max(ans, xor())
        return
    
    selected.append(num_list[curr_num])
    choose(cnt + 1, curr_num + 1)
    selected.pop()

    choose(cnt, curr_num + 1)


choose(0, 0)
print(ans)