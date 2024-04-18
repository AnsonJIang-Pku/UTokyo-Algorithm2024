# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/171478
N, K = map(int, input().split())
M = 998244353
MAX = 200010
# use dp
factorial = [1] * MAX
for i in range(1, MAX):
    factorial[i] = factorial[i-1] * i % M

def iter_pow(base, power):
    ans = 1
    while power > 1:
        if power % 2:
            ans *= base % M
        base = base * base % M
        power = power // 2
    return ans * base % M


def r_combinatorial(n, k):
    return (factorial[n] % M) * (iter_pow(factorial[n-k], M-2) % M) * (iter_pow(factorial[k], M-2) % M) % M

print(r_combinatorial(N,K))
