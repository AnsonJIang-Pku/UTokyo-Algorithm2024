# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/176777
class Hash_table:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size

    def insert(self, x: int):
        index = x % self.size
        if self.table[index] == -1:
            self.table[index] = x
        else:
            old_index = index #保存初始index，用来判断是否满
            while self.table[index] != -1:
                index = (index+1) % self.size
                if index == old_index:
                    print("full")
                    break
            self.table[index] = x
        
    def search(self, x: int):
        index = x % self.size
        if self.table[index] == x:
            print("found")
        else: #index处存的是别的值，线性探索
            while self.table[index] != x:
                if self.table[index] == -1:
                    print("not found")
                    break
                elif self.table[index] == x:
                    print("found")
                else:
                    index = (index+1) % self.size
                    if index == x % self.size:
                        print("not found")
                        break
            if self.table[index] == x:
                print("found")
            
Q = int(input())
ht = Hash_table(Q)
for i in range(Q):
    oper = list(map(int, input().split()))
    if oper[0] == 0:
        ht.insert(oper[1])
    else:
        ht.search(oper[1])
