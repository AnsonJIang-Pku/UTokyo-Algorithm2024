#最终提交版
# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/174045
#总结：考察了对于流数据中的中位数的处理（最大堆+最小堆）（leetcode 295 hard），和如何将这种特殊的函数|x-a_i|求和转化为O(1)复杂度的计算
class BasicMin_heap:
    def __init__(self, size):
        self.inf = 10 ** 9
        self.size = size + 1
        self.array = [self.inf] * size
        self.last = 0
    
    def add(self, x: int):
        if self.last != self.size:
            self.last += 1
            self.array[self.last] = x
            self.check_after_add(self.last)

    def check_after_add(self, index):
        if index <= 1:
            return 
        if self.array[index // 2] > self.array[index]:
            self.array[index//2], self.array[index] = self.array[index] , self.array[index//2]
            self.check_after_add(index//2)
        
    def remove(self):
        if self.last != 0:
            temp = self.array[1]
            self.array[1] = self.array[self.last]
            self.array[self.last] = self.inf
            self.last -= 1
            self.check_after_remove(1)
            return temp
    
    def check_after_remove(self, index):
        left_child, right_child = 2 * index, 2 * index + 1
        min_child = index
        if left_child <= self.last and self.array[left_child] < self.array[min_child]:
            min_child = left_child
        if right_child <= self.last and self.array[right_child] < self.array[min_child]:
            min_child = right_child
        if min_child != index:
            self.array[index], self.array[min_child] = self.array[min_child], self.array[index]
            self.check_after_remove(min_child) #之前这里写成了2 * index, 有可能是2 * index + 1啊!!!

class Myheap:
    def __init__(self):
        #使用最大堆和最小堆实现查找中位数
        self.max_heap = BasicMin_heap(100010) 
        #用来存较小的一半数字,heapq中只有最小堆,因此这部分值是相反数
        #取出的时候再取相反数
        self.min_heap = BasicMin_heap(100010) #用来存较大的一半数字
        self.sum = 0

    #取中位数的函数
    def fetch_median(self):
        if self.max_heap.last > self.min_heap.last:
            median = - self.max_heap.array[1] 
        else:
            median = self.min_heap.array[1]
        return median
    
    #求绝对值和的函数(偏移求和)
    def summation(self, new_median, old_median):
        delta = abs(new_median - old_median)
        Nmax_heap, Nmin_heap = self.max_heap.last, self.min_heap.last
        #排除initial case
        if not (Nmin_heap and Nmax_heap):#如果二者中有一个为0
            return 
        
        #经过分析, 如果新中位数在min堆，只能是old_median < new_median
        #如果新中位数在max堆，只能是new_median < old_median
        if new_median < old_median:
            #哪个需要减1要看中位数在哪边
            self.sum += - (Nmax_heap - 1) * delta + Nmin_heap * delta
        else:
            self.sum +=  Nmax_heap * delta - (Nmin_heap - 1) * delta

    def push(self, x: int):
        #记录旧的中位数，用于O(1)求和
        if not self.max_heap.last:
            old_median = 0 #最大堆中一定得有数，否则就是initial case
        else:
            #中位数不一定是max_heap里的(依赖于堆的建立过程)
            old_median = self.fetch_median()

        #如果x比最小堆的最小值还大,那么不能插入最大堆
        if self.min_heap.last and x > self.min_heap.array[1]:
            self.min_heap.add(x)
        else:
            self.max_heap.add(-x) #向最大堆中加入-x
        #是否向最小堆中移动值
        if self.max_heap.last > self.min_heap.last + 1:
            temp = - self.max_heap.remove()
            self.min_heap.add(temp)
        #是否向最大堆中移动值
        if self.min_heap.last > self.max_heap.last + 1:
            temp = - self.min_heap.remove()
            self.max_heap.add(temp)

        #计算新的sum O(1)
        #新中位数不一定是max_heap里的
        new_median = self.fetch_median()
        #如果新加入的数不充当中位数, 还要加上新的差值
        if x != new_median and x != old_median:
            self.sum += abs(x - new_median)
        #利用变化求和,而不是去遍历
        #Helper function
        self.summation(new_median, old_median)
        
    def query(self):
        if self.max_heap.last == 0 or self.min_heap.last == 0:
            print(0)
            return 
        print(self.sum)
        return 

Q = int(input())
myheap = Myheap()
for i in range(Q):
    oper = list(map(int, input().split()))
    if oper[0] == 1:
        myheap.push(oper[1])
    elif oper[0] == 2:
        myheap.query()
