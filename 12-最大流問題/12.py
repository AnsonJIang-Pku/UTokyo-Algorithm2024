# 最大流问题
N, M = map(int, input().split())
capacity = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    capacity[u][v] = c

max_flow = 0

def dfs(s, e, flow):
    global visited
    if (s == e):
        return flow
    visited[s] = True

    for i in range(1, N+1):
        if not visited[i] and capacity[s][i] > 0:
            f = dfs(i, N, min(capacity[s][i], flow))
            if f > 0:
                capacity[s][i] -= f
                capacity[i][s] += f
                return f
    return 0

while True:
    visited = [False] * (N+1)
    f = dfs(1, N, 10 ** 9)
    if not f:
        break
    max_flow += f

print(max_flow)
