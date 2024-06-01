# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/184313
N = int(input())
h = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
dp[2] = abs(h[1] - h[2])
for i in range(3, N+1):
    dp[i] = min(dp[i-1] + abs(h[i-1] - h[i]), dp[i-2] + abs(h[i-2] - h[i]))

print(dp[N])
