#超时解2，使用heap
import heapq
class Myheap:
    def __init__(self):
        #使用最大堆和最小堆实现查找中位数
        self.max_heap = [] 
        #用来存较小的一半数字,heapq中只有最小堆,因此这部分值是相反数
        #取出的时候再取相反数
        self.min_heap = [] #用来存较大的一半数字
    
    def push(self, x: int):
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

    def query(self):
        if len(self.max_heap) == 0 or len(self.min_heap) == 0:
            print(0)
            return 
        #先不考虑奇偶数个元素，用max_heap[0]当作中位数
        mid1, mid2 = -self.max_heap[0], self.min_heap[0]
        tempList = list(map(lambda x: -x, self.max_heap)) + self.min_heap
        sum1, sum2 = 0, 0
        for x in tempList:
            sum1 += abs(mid1 - x)
            sum2 += abs(mid2 - x)
        #这里要确定到底选哪个值
        print(min(sum1, sum2))
        return 

Q = int(input())
myheap = Myheap()
for i in range(Q):
    oper = list(map(int, input().split()))
    if oper[0] == 1:
        myheap.push(oper[1])
    elif oper[0] == 2:
        myheap.query()

