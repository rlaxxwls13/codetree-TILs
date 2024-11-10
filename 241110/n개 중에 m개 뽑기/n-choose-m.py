n, m = map(int, input().split())

answer = []

def print_list():
    for element in answer:
        print(element, end=" ")
    print()


def choose(cnt, curr_num):
    if cnt == m:
        print_list()
        return
    for i in range(1, n+1):
        if i > curr_num:
            answer.append(i)
            choose(cnt + 1, i)
            answer.pop()
    return

choose(0, 0)