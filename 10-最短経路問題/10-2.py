# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/192644

N, M = map(int, input().split())

# 初始化dist矩阵, dist[i][j]存储从顶点i到j的最短路径
dist = [[float('inf')] * N for _ in range(N)]

for _ in range(M):
    temp = list(map(int, input().split()))
    dist[temp[0]][temp[1]] = temp[2]

for i in range(N):
    dist[i][i] = 0

# Floyd算法
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 处理query
Q = int(input())
for i in range(Q):
    u, v = map(int, input().split())
    if dist[u][v] != float('inf'):
        print(dist[u][v])
    else:
        print("INF")
