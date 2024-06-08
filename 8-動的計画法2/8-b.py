# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/187973
N, K = map(int, input().split())
a = [0] + list(map(int, input().split()))
SIZE = 998244353

dp = [[0 for _ in range (K+1)] for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 1 #给前i个孩子分0个糖,只有一种方法 dp[0][0]=1!!

# 更新dp表
for i in range(1, N+1): #对于每一行
    # 首先用前一行的结果计算前缀和
    prefix_sum = [dp[i-1][0]] # 下标从0开始
    for j in range(1,K+1):
        prefix_sum.append(prefix_sum[j-1] + dp[i-1][j])
    # 利用前缀和数组更新每一行的dp表,
    for j in range(1, K+1):
        if j - a[i] <= 0:
            dp[i][j] = prefix_sum[j]
        else:
            dp[i][j] = prefix_sum[j] - prefix_sum[j-a[i]-1]

print(dp[N][K] % SIZE)
