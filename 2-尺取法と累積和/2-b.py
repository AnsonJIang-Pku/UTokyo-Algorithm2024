# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/171479
Q = int(input())
# cal the primes before
max_r = 2000010
is_primes = [True] * (max_r + 1)
i = 2
while i * i <= max_r:
    if is_primes[i]:
        j, k = i, 2
        while True:
            j = k * i
            if j <= max_r:
                is_primes[j] = False
                k += 1
            else:
                break
    i += 1
is_primes[0], is_primes[1] = False, False
ls = [False] * max_r
for x in range(1, max_r):
    if x % 2 and is_primes[x] and is_primes[(x+1)//2]:
        ls[x] = True

acc = [0] * max_r
for i in range(1, max_r):
    acc[i] = acc[i-1] + ls[i]

for _ in range(Q):
    l, r = map(int, input().split())
    ans = acc[r] - acc[l-1]
    print(ans)
