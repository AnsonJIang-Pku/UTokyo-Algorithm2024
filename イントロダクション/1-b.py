# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/165732
N, M = map(int, input().split())
ls = list(map(int, input().split()))
index, sum = 1, 0
for i in range(M):
    sum += ls[i]
    now = sum
for i in range(N - M):
    now = now - ls[i] + ls[i + M]
    if now > sum:
        index = i + 2
        sum = now
print(sum, index, end = ' ')
