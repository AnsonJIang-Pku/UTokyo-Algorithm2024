# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/184314
N, S = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j]代表考虑了前i个元素时,能组成总和为j, boolean
dp = [ [False for _ in range(S+1)] for _ in range(N+1) ]
#注意不能用[[False]*(S+1)] * (N+1)，因为这样的话每个子列表都是同一个（互为引用）

# initialize
dp[0][0] = True # 什么都不放时，能达到总和为0

# 更新dp表
for i in range(0, N):
    for j in range(S+1):
        if j >= A[i]:
            dp[i+1][j] = dp[i][j-A[i]] or dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]

if dp[N][S]:
    print("Yes")
else:
    print("No")
