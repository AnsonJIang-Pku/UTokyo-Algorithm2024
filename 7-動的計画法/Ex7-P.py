# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/184315
# 30/30：优化掉不需要的体力
# 需要用三维动态规划，因为有三个状态变量
# 不能用dp[i][j]存[方法数,剩余体力]，因为对于每条路径剩余的体力都不一定一样
# dp[i][j][k] = 在(i,j)时，剩余体力为k的所有可能方法数
# 发现dp表可以状态压缩(把行状态压缩到循环里)

H, W, P = map(int, input().split())
N = int(input())

restore = {} # 直接存成字典,存储所有有补充体力格子的体力值 restore[(i,j)] = p
suml = 0
for i in range(N):
    temp = list(map(int, input().split()))
    x, y, energy= temp[0], temp[1], temp[2]
    min_energy = H + W - (x+y) # 足够走到最后的最小体力
    energy = min(energy, min_energy)
    restore[tuple([x, y])] = energy
    suml += energy
maxp = H+W # 最大体力就只可能是这个，如果途中加到比这个大就改成这个
P = min(H+W-2, P)

# 初始化dp数组
# 最里面是最后一维
dp = [[0 for _ in range(maxp+1)] for _ in range(W+1)]
#initialize
dp[1][P] = 1

# 更新dp数组, 按行从左到右更新
for i in range(1, H+1): # 从第1行开始,更新H次
    for j in range(1, W): # 从第1列开始,更新W次
        for k in range(1, maxp+1):
            # 第一行特殊更新(j=1格子不更新自己)
            if i == 1:
                if k and dp[j][k] != 0:
                    if (i,j+1) in restore:
                        p = restore[(i, j+1)]
                        dp[j+1][min(k-1+p, maxp)] += dp[j][k]
                    else:
                        dp[j+1][k-1] += dp[j][k]
            # i不为1,要用到备份格子temp       
            else:
                # 需要对第一个dp[1]完全更新完后才能继续
                if j == 1 and k == 1: # 特殊更新第一列,因为不能从左格子来
                    # 先创建当前格子的备份
                    now = [x for x in dp[j]]
                    # 先清零当前dp[j]所有元素,避免干扰
                    dp[j] = [0] * (maxp+1)
                    for l in range(1, maxp+1):
                        if now[l] != 0:
                            if (i, j) in restore:
                                p = restore[(i, j)]
                                dp[j][min(l-1+p, maxp)] += now[l]
                            else:
                                dp[j][l-1] += now[l]
                    
                # 即使是第一列,也可以向右走
                if k == 1:
                    # 备份dp[j+1]
                    temp = [x for x in dp[j+1]]
                    # 清零右边dp[j+1]格子
                    dp[j+1] = [0] * (maxp+1)
                if temp[k] != 0 or dp[j][k] != 0: # 可以走
                    if (i,j+1) in restore:
                        p = restore[(i,j+1)]
                        dp[j+1][min(k-1+p, maxp)] += temp[k]
                        dp[j+1][min(k-1+p, maxp)] += dp[j][k]
                    else:
                        dp[j+1][k-1] += temp[k]
                        dp[j+1][k-1] += dp[j][k]
                    

SIZE = 998244353
ans = 0
for x in dp[W]:
    ans = (ans + x) % SIZE
print(ans)
