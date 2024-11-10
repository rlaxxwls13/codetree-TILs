n = int(input())
visited = [False for _ in range(n+1)]
permutation = []

def print_number():
    for element in permutation:
        print(element, end=" ")
    print()

def choose(cnt):
    if cnt == n:
        print_number()

    for i in range(1, n+1):
        if visited[i] == True:
            continue
        visited[i] = True
        permutation.append(i)
        choose(cnt + 1)
        visited[i] = False
        permutation.pop()
    return

choose(0)