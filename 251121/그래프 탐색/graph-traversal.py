n, m = tuple(map(int, input().split()))
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

visited = [False for _ in range(n + 1)]
ans = 0

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(vertex):
    global ans
    for curr in range(1, n+1):
        if graph[vertex][curr] == 1 and not visited[curr]:
            visited[curr] = True
            ans += 1
            dfs(curr)

visited[1] = True
dfs(1)
print(ans)
            
    