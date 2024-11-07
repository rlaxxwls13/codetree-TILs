K, N = map(int, input().split())
answer = []

def print_answer(answer):
    for x in answer:
        print(x, end=" ")
    print()

def choose(curr_num):
    if curr_num == N + 1:
        print_answer(answer)
        return
    for i in range(1, K+1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()
    return

choose(1)