# 폭탄의 종류
bomb_type = [[[-2,0],[-1,0],[0,0],[1,0],[2,0]], [[-1,0],[0,-1],[0,0],[0,1],[1,0]], [[-1,-1],[-1,1],[0,0],[1,-1],[1,1]]]

# 폭탄 위치와 종류를 주면 초토화된 영역 리턴
def apply_bomb(loc, bomb):
    # bomb ex: [[-2,0],[-1,0],[0,0],[1,0],[2,0]]
    # loc ex: [1,1]
    # bomb 각각에 curr_location을 더해서 리턴해야함
    # 더했을때 0<=index<n이어야함
    result = []
    for bomb_area in bomb:
        result.append(list(map(sum, zip(loc, bomb_area))))
    return list(filter(lambda x: x[0] < n and x[0] >= 0 and x[1] >= 0 and x[1] < n, result))
    #return list(map(lambda x: list(map(sum, zip(x, bomb_location[curr_location]))), bomb))

def count_area(bomb_area):
    result = []
    for i in bomb_area:
        for j in i:
            result.append(j)
    return len(set(tuple(x) for x in result))

def select_bomb(curr_num):
    # curr_num이 폭탄위치의 개수보다 커지면 초토와된 영역 수 리턴
    if curr_num == len(bomb_location):
        count.append(count_area(bomb_area))
        return
    # for문을 돌리면서 각각의 폭탄 적용해봄
    for bomb in bomb_type:
        # 해당 폭탄 적용
        # 리스트에 현재 폭탄이 초토화한 영역 리스트를 추가함, 총 초토화한 영역 계산은(중복 포함) 재귀문 마지막에 함
        bomb_area.append(apply_bomb(bomb_location[curr_num], bomb))
        # 그다음 재귀문으로
        select_bomb(curr_num + 1)
        bomb_area.pop()
    return


n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]

# 초토화된 영역
bomb_area = []

# 초토화된 영역의 수
count = []

# 폭탄의 위치
bomb_location = []

# 폭탄 위치를 저장해둠
for i in range(n):
    for j in range(n):
        if L[i][j] == 1:
            bomb_location.append([i, j])


select_bomb(0)
print(max(count))