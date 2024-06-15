# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/191031
# 实在不知道为什么还超时，应该不是分解质因数的问题
import math
from collections import deque
from collections import Counter
SIZE = 998244353
MAX_NUM = 100010

N = int(input())
A = [0] + list(map(int, input().split())) # 下标从1开始
graph = [[] for _ in range(N+1)] #邻接表，下标从1开始
for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 分解质因数
def spf(n):
    spf = [_ for _ in range(n+1)]
    i = 2
    while i * i <= n:
        if spf[i] == i:
            j = 2 * i
            while j <= n:
                if spf[j] == j:
                    spf[j] = i
                j += i
        i += 1
    return spf

spf = spf(MAX_NUM)
factor_cache = [0] * MAX_NUM
# 质因数分解
def prime_factors(n):
    original_n = n
    if factor_cache[n] != 0:
        return factor_cache[n]
    factors = Counter()
    while n > 1:
        if factor_cache[n] != 0:
            factor_cache[original_n] = factors + factor_cache[n]
            return factor_cache[original_n]
        factors[spf[n]] += 1
        n //= spf[n]
    factor_cache[original_n] = factors
    return factors

# 递归写法，可以存储路径上的结果
# def prime_factors(n):
#     if factor_cache[n] != 0:
#         return factor_cache[n]
#     if n == 1:
#         return Counter([])
#     factor_cache[n] = Counter([spf[n]]) + prime_factors(n // spf[n])
#     return factor_cache[n]

# 预处理每个节点,分解质因数
for i in range(1, N+1):
    A[i] = prime_factors(A[i])

# 给一个counter,求出(e_1+1)(e_2+1)...(e_n+1)
def num(node_factor):
    count = 1
    for val in node_factor.values():
        count = count * (val + 1)
    return count

# BFS求最短路径
visited = [0 for _ in range(N+1)] # 下标从1开始,也是结果

# 初始化
fringe = deque([1])
visited[1] = num(A[1])
while fringe:
    now = fringe.popleft()
    for u in graph[now]:
        if not visited[u]:
            A[u] = A[now] + A[u]
            visited[u] = num(A[u]) % SIZE
            fringe.append(u)
    A[now] = 0

for i in range(1, N+1):
    print(visited[i])
