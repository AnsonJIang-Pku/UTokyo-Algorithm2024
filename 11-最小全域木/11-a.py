# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/193686
# 并查集
class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.height = [0 for i in range(N)]
    
    def root(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def connect(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x != root_y:
            if self.height[x] < self.height[y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                if self.height[root_x] == self.height[root_y]:
                    self.height[root_x] += 1
    
    def is_connected(self, x, y):
        if self.root(x) == self.root(y):
            return True
        else:
            return False

# Kruskal最小生成树
N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, d = map(int, input().split())
    edges.append([d, a, b])
edges.sort()

# 初始化并查集
ufs = UnionFind(N)
mst = [] # 最小生成树
cost = 0

for e in edges:
    if not ufs.is_connected(e[1], e[2]):
        ufs.connect(e[1], e[2])
        mst.append([e[1], e[2]])
        cost += e[0]

print(cost)
