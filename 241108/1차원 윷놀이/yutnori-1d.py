n, m, k = map(int, input().split())
dist_list = list(map(int, input().split()))
selected = []
location = [1 for _ in range(k)]
mx = 0

def score():
    result = 0
    for x in location:
        if x >= m:
            result += 1
    return result

# 움직일 말을 선택하다가 전부 선택하면 return
# m에 도달한 말이거나 해당 말을 현재 숫자만큼 움직였을때 m을 넘어가면 움직이지 x

def choose(cnt):
    global mx

    # cnt 끝까지 가지 않더라도 최대가 될 수 있으므로 항상 답을 갱신함
    mx = max(score(), mx)
    if cnt == n:
        return

    for i in range(k):
        # 전부 m을 넘을때 cnt 끝까지 못가고 끝나버리는 문제가 ...
        if location[i] >= m:
            continue
        location[i] += dist_list[cnt]
        choose(cnt + 1)
        location[i] -= dist_list[cnt]
    return

choose(0)
print(mx)