# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/165731
M, L = map(int, input().split())
N = int(input())
for i in range(N):
    name, *list = input().split()
    price, level = map(int, list)
    if price <= M and L >= level:
        print(name, price, end = ' ')
        print()
