# 10/30三维动态规划，空间超
# 需要用三维动态规划，因为有三个状态变量
# 不能用dp[i][j]存[方法数,剩余体力]，因为对于每条路径剩余的体力都不一定一样
# dp[i][j][k] = 在(i,j)时，剩余体力为k的所有可能方法数

H, W, P = map(int, input().split())
N = int(input())

restore = {} # 直接存成字典,存储所有有补充体力格子的体力值 restore[(i,j)] = p
maxp = -1 # 为了看初始化体力的维度最大为多少
suml = 0
for i in range(N):
    temp = list(map(int, input().split()))
    restore[tuple([temp[0], temp[1]])] = temp[2]
    maxp = max(maxp, temp[2])
    suml += temp[2]
maxp = suml


# 初始化dp数组
# 最里面是最后一维
dp = [[[0 for _ in range(maxp+1)] for _ in range(W+1)] for _ in range(H+1)]
#initialize
dp[1][1][P] = 1

# 更新dp数组, 按行从左到右更新
for i in range(1, H+1):
    for j in range(1, W+1):
        for k in range(1, maxp+1):
            if k and dp[i][j][k] != 0: # 如果当前格子的体力不为0且方法不为0，可以继续向右走和向下走
                # 向右走
                if j < W:
                    if (i, j+1) in restore: # 加体力
                        p = restore[(i, j+1)]
                        dp[i][j+1][k-1+p] += dp[i][j][k]
                    else:
                        dp[i][j+1][k-1] += dp[i][j][k]
                #向下走
                if i < H:
                    if (i+1, j) in restore: #加体力
                        p = restore[(i+1, j)]
                        dp[i+1][j][k-1+p] += dp[i][j][k]
                    else:
                        dp[i+1][j][k-1] += dp[i][j][k]

SIZE = 998244353
ans = 0
for x in dp[H][W]:
    ans = (ans + x) % SIZE
print(ans)
