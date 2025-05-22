n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
ans = 0
curr = 1
visited = [False for _ in range(n+1)]
visited[curr] = True

def dfs(vertex):
    global ans
    for edge in edges:
        if edge[0] == vertex and visited[edge[1]] == False:
            ans += 1
            visited[edge[1]] = True
            dfs(edge[1])
        elif edge[1] == vertex and visited[edge[0]] == False:
            ans += 1
            visited[edge[0]] = True
            dfs(edge[0])

dfs(curr)
print(ans)


