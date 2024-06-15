# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/191030
from collections import deque
# 双端队列append()队尾添加元素, popleft()队头弹出元素

H, W = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
maze = [[0] for _ in range(H+1)] # 坐标从1开始
for i in range(1, H+1):
    temp = list(input())
    maze[i].extend(temp)

directions = [[1,0], [-1,0], [0,1], [0,-1]]
visited = [[False] * (W+1) for _ in range(H+1)] # 存储访问过与否
dist = [[-1] * (W+1) for _ in range(H+1)] # 存储最短距离
# 初始化
fringe = deque([[sx, sy]])
visited[sx][sy], dist[sx][sy] = True, 0
while fringe:
    now = fringe.popleft()
    if now == [gx, gy]:
        print(dist[gx][gy])
        break
    for d in directions:
        next_x, next_y = now[0] + d[0], now[1] + d[1]
        if 0 < next_x < H+1 and 0 < next_y < W+1:
            if not visited[next_x][next_y] and maze[next_x][next_y] == '.':
                dist[next_x][next_y] = dist[now[0]][now[1]] + 1
                visited[next_x][next_y] = True
                fringe.append([next_x, next_y])
