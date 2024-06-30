#source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/192643

import heapq

N, M, S = map(int, input().split())
# 注意是有向图
graph = [[] for _ in range(N)] # 共有N个顶点, 顶点i的格式graph[i] : [[邻边, cost], ...]
for _ in range(M):
    temp = list(map(int, input().split()))
    graph[temp[0]].append([temp[1], temp[2]])

done = [False] * N
dist = [float('inf')] * N
dist[S] = 0
PQ = []

def dijkstra(graph, S):
    heapq.heappush(PQ, [dist[S], S]) #优先队列中元素格式[目前距离, #node]
    while PQ:
        now = heapq.heappop(PQ)
        cur_node = now[1]
        if not done[cur_node]:
            for edge in graph[cur_node]:
                if dist[edge[0]] > dist[cur_node] + edge[1]:
                    dist[edge[0]] = dist[cur_node] + edge[1]
                    heapq.heappush(PQ, [dist[edge[0]], edge[0]])
        done[cur_node] = True

dijkstra(graph, S)
for i in range(N):
    if dist[i] != float('inf'):
        print(dist[i])
    else:
        print("INF")
