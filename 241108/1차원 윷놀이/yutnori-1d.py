n, m, k = map(int, input().split())
dist_list = list(map(int, input().split()))
selected = []
location = [1 for _ in range(k+1)]
mx = 0

def print_selected():
    for x in selected:
        print(x, end=" ")
    print()

def score():
    result = 0
    for x in location:
        if x >= 6:
            result += 1
    return result

# 움직일 말을 선택하다가 전부 선택하면 return
# m에 도달한 말이거나 해당 말을 현재 숫자만큼 움직였을때 m을 넘어가면 움직이지 x

def choose(cnt):
    global mx
    if cnt == n:
        if score() > mx:
            mx = score()
        return
    for i in range(1, k+1):
        if location[i] >= m:
            continue
        selected.append(i)
        location[i] += dist_list[cnt]
        choose(cnt + 1)
        selected.pop()
        location[i] -= dist_list[cnt]
    return

choose(0)
print(mx)