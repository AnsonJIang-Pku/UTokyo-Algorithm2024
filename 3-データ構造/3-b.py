# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/174319
class Maxheap:
    def __init__(self, size):
        self.size = size + 1 #不用列表的第0项
        self.inf = - 10 ** 9 #一个很小的数(max heap)
        self.last = 0 #最后一个元素的位置
        self.array = [self.inf] * self.size

    def add(self, x: int):
        if self.last < self.size - 1:
            self.last += 1
            self.array[self.last] = x
            self.check_after_add(self.last) #检查堆结构是否保持

    def check_after_add(self, index):
        if index == 1:
            return
        if self.array[index//2] < self.array[index]:
            self.array[index], self.array[index//2] = self.array[index//2], self.array[index]
            self.check_after_add(index//2)
    
    def remove(self):
        if self.last > 0:
            temp = self.array[1]
            print(temp)
            self.array[1] = self.array[self.last]
            self.array[self.last] = self.inf
            self.last -= 1
            self.check_after_remove(1) #检查堆结构是否保持
            return temp

    def check_after_remove(self, index):
        left_child, right_child = 2 * index, 2 * index + 1
        max_child = index
        if left_child <= self.last and self.array[left_child] > self.array[max_child]:
            max_child = left_child
        if right_child <= self.last and self.array[right_child] > self.array[max_child]:
            max_child = right_child
        if max_child != index:
            self.array[index], self.array[max_child] = self.array[max_child], self.array[index]
            self.check_after_remove(max_child) #之前这里写成了2 * index, 有可能是2 * index + 1啊!!!

Q = int(input())
#initialize max heap
mheap = Maxheap(Q + 10)
for i in range(Q):
    oper = list(map(int, input().split()))
    if oper[0] == 1:
        mheap.add(oper[1])
    elif oper[0] == 2:
        mheap.remove()
