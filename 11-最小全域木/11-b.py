# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/193687

from collections import deque
import heapq

N, M = map(int, input().split())

# 初始化
indeg = [0] * N
outedge = [[] for _ in range(N)] # 邻接表
for i in range(M):
    u, v = map(int, input().split())
    outedge[u].append(v)
    indeg[v] += 1

init = [i for i in range(N) if indeg[i] == 0] 
waitlist = [] # heap
for ele in init:
    heapq.heappush(waitlist, ele)
sorted_g = [] # 存储结果

while waitlist:
    now = heapq.heappop(waitlist)
    # if indeg[now] == 0:
    sorted_g.append(now)
    for next_node in outedge[now]:
        indeg[next_node] -= 1
        M -= 1 # 判断图是不是DAG
        if indeg[next_node] == 0:
            heapq.heappush(waitlist, next_node)
            
if M:
    print("-1")
else:
    for ele in sorted_g:
        print(ele, end=' ')
