# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/171781
import numpy as np
N = int(input())
x = [0]
x = x + list(map(int, input().split())) #to maintain index start from 1
Q = int(input())
# Preprocessing, transform sigma.
# cal two acculumations
x = np.array(x) # x_acc[i] = x[1] + x[2] + ... + x[i]
x_acc = np.cumsum(x)
lin_ls = np.arange(0, N+1) # mul_acc[i] = x[1]*1 + x[2]*2 + ... + x[i]*i
mul_acc = lin_ls * x
mul_acc = np.cumsum(mul_acc)

for i in range(Q):
    L, R, A, B = map(int, input().split())
    #注意哪一步最耗时间复杂度，调整需要运算的顺序
    sum1 = (mul_acc[R] - mul_acc[L-1]) * A
    sum2 = (x_acc[R] - x_acc[L-1]) * B
    print(sum1 + sum2)
