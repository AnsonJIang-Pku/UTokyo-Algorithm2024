# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/181726
# 17/30不知道怎么优化了
from collections import Counter
# Counter类可以认为是加强版字典,支持 +,-,|,&,...,total()

N = int(input()) # 有N个正整数数列V_1,...,V_N
K = [0] * (N+1)  # K[i]代表数列V_i的长度
# V[0] is a dumb array
V = [[0]] # V[i]代表第i个数列, V[i][j]代表第i个数列V[i]的第j个元素
# Modified:
D = [[0]] # 存储Counter对象, D[i]代表第i个小数组的Counter对象
# 但是每个数列本身是从0开始的
for i in range(1, N+1):
    K[i] = int(input())
    V.append(list(map(int, input().split())))
    #将输入的数组转化为Counter
    D.append(Counter(V[i]))

# 想法：输入的时候就将每个小数组转化成字典，最后查询的时候只要拼接他们

#我觉得问题出在这里，其实可以不用字典，而且不用合并数组
def is_equivalent(num1: int, group1: list, num2: int, group2: list):
    # 如何设计list实现,不用字典?
    counter1 = Counter({0: 0})
    for i in range(num1):
        ngroup = group1[i]
        counter1 += D[ngroup]
    counter2 = Counter({0: 0})
    for i in range(num2):
        ngroup = group2[i]
        counter2 += D[ngroup]

    if counter1 == counter2:
        print("Yes")
    else:
        print("No")

Q = int(input())
for i in range(Q):
    num1 = int(input())
    group1 = list(map(int, input().split()))
    num2 = int(input())
    group2 = list(map(int, input().split()))
    is_equivalent(num1, group1, num2, group2)
