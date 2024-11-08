K, N = map(int, input().split())
selected = []

def print_list():
    for x in selected:
        print(x, end=" ")
    print()

def choose(curr_num):
    if curr_num == N+1:
        print_list()
        return

    for i in range(1, K+1):
        if len(selected) >= 2 and selected[curr_num-1] == i and selected[curr_num-2] == i:
            break
        selected.append(i)
        choose(curr_num+1)
        selected.pop()
    return

choose(1)