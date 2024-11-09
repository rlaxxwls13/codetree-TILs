n = int(input())
number_list = [tuple(map(int, input().split())) for _ in range(n)]
dir_list = [tuple(map(int, input().split())) for _ in range(n)]
curr_loc = tuple(map(lambda x: int(x) - 1, input().split()))

direction = [(0,0),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

ans = 0
cnt = 0

# 더이상 이동할수있는 숫자가 없을 떄 멈춤
# 현재 위치: number_list[r][c]
# 현재 위치에서 이동할 수 있는 곳을 계산하는 함수

# 함수 시작하면 인자인 curr_loc에서 이동할수있는 인덱스를 계산함
# 해당 인덱스가 없으면 리턴
# 인덱스가 있으면 그 인덱스 리스트에서 포문을 돌려서 이동하고 다음 재귀문으로 이동
# max값은 항상 갱신?아닐거같은데
# 아까는 재귀문이 끝나는 조건일때까지 다다르지 않고 끝날때도 있어서 매번 최댓값을 갱신했는데 
# 이 문제는 재귀문 종료 조건일때 최댓값이어서 항상 갱신할 필요 없음

# 현재 위치에 direction[현재방향]의 배수만큼 만큼 더해서 갈수있는 인덱스를 구함
# 갈수있는 인덱스중에 그 인덱스에 해당하는 숫자가 현재 위치에 있는 숫자보다 크면 result에 append함
# 몇배까지 할건지 정해야됨.. 최대 이동할수있는건 아마 n-1만큼 그리고 이동했을때 0과n사이가 아니면 pass

def can_go(curr_loc):
    result = []
    curr_r = curr_loc[0]
    curr_c = curr_loc[1]
    curr_num = number_list[curr_r][curr_c]
    dir = direction[dir_list[curr_r][curr_c]]
    for i in range(1,n):
        next_r = curr_r + i * dir[0]
        next_c = curr_c + i * dir[1]
        if next_r >= 0 and next_r < n and next_c >= 0 and next_c < n:
            if number_list[next_r][next_c] > curr_num:
                result.append((next_r,next_c))
        else:
            break  
    return result


def choose(curr_loc):
    global ans, cnt
    
    if not can_go(curr_loc):
        ans = max(ans, cnt)
        return

    for next_loc in can_go(curr_loc):
        cnt += 1
        choose(next_loc)
        cnt -= 1
    return

choose(curr_loc)
print(ans)