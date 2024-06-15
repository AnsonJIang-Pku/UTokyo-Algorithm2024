# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/191029
import sys
import resource

sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))

N, M, S, T = map(int, input().split())
edge = [-1] + [[] for _ in range(N)]  # 下标从1开始，为了匹配S和T
# 转化为邻接表（无向图版本）
for i in range(M):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

# implement DFS by recursion
visited = [0] + [False] * N # 下标从1开始
def dfs(edge, s, t):
    # 剪枝,不做多余工作
    if visited[0] == 1:
        return
    visited[s] = True
    if s == t:
        print("Yes")
        visited[0] = 1 # 记录已经输出了Yes，访问成功
        return 
    # 遍历s的所有未访问邻边
    for e in edge[s]:
        if not visited[e]:
            dfs(edge, e, t)

dfs(edge, S, T)
if visited[0] == 0:
    print("No")
