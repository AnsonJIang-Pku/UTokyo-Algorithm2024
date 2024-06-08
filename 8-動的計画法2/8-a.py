# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/187972
# 大0-1背包问题
# 读取输入数据
N, W = map(int, input().split())
w, v = [-1], [-1] #物品编号从1开始
maxv, minv = 0, 0
for i in range(N):
    temp = list(map(int, input().split()))
    w.append(temp[0])
    v.append(temp[1])
    maxv += temp[1]
    minv = min(minv, temp[1])

MAX = 10 ** 9 + 10

#初始化dp表, dp[i][j]存放: 考虑了前i个物品, 总价值为j时的最小总重量
dp = [[MAX for _ in range(maxv+1)] for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 0 # 没有总价值时,min总重一定为0
# for j in range(maxv+1):
#     dp[0][j] = 0 # 没有物品放入时,min总重一定为0

for i in range(1, N+1):
    for j in range(1, maxv+1):
        if j >= v[i]:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i]] + w[i])
        else:
            dp[i][j] = dp[i-1][j]
# 寻找目标值:满足dp[N][j] <= W时, 总价最大的j
for j in range(maxv, 0, -1):
    if dp[N][j] <= W:
        print(j) #一开始这里写错了。。。
        break
