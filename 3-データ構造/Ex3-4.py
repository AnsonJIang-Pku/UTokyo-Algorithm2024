#AC，但是用到heapq库
import heapq
class Myheap:
    def __init__(self):
        #使用最大堆和最小堆实现查找中位数
        self.max_heap = [] 
        #用来存较小的一半数字,heapq中只有最小堆,因此这部分值是相反数
        #取出的时候再取相反数
        self.min_heap = [] #用来存较大的一半数字
        self.sum = 0

    #取中位数的函数
    def fetch_median(self):
        if len(self.max_heap) > len(self.min_heap):
            median = - self.max_heap[0] 
        else:
            median = self.min_heap[0]
        return median
    
    #bug
    #求绝对值和的函数(偏移求和)
    def summation(self, new_median, old_median):
        delta = abs(new_median - old_median)
        Nmax_heap, Nmin_heap = len(self.max_heap), len(self.min_heap)
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
        if not len(self.max_heap):
            old_median = 0 #最大堆中一定得有数，否则就是initial case
        else:
            #中位数不一定是max_heap里的(依赖于堆的建立过程)
            old_median = self.fetch_median()

        #如果x比最小堆的最小值还大,那么不能插入最大堆
        if len(self.min_heap) and x > self.min_heap[0]:
            heapq.heappush(self.min_heap, x)
        else:
            heapq.heappush(self.max_heap, -x) #先向最大堆中加入-x
        #是否向最小堆中移动值
        if len(self.max_heap) > len(self.min_heap) + 1:
            temp = - heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, temp)
        #是否向最大堆中移动值
        if len(self.min_heap) > len(self.max_heap) + 1:
            temp = - heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, temp)

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
        if len(self.max_heap) == 0 or len(self.min_heap) == 0:
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

