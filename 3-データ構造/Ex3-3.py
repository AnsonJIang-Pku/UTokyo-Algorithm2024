#优化了求新的sum的过程，感谢cdm
# 微微超时解 26/30
class MyList:
    def __init__(self, size):
        self.last = 0 #待插入元素的位置，也是现在数组中元素的个数
        self.array = [None] * size
        self.sum = 0

    def binarysearch_push(self, x: int):
        if self.last:
            old_median = self.array[self.last // 2] #记录插入之前的中位数
        else:
            old_median = 0
        low, high = 0, self.last - 1
        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        self.array.insert(low, x) # 这里应该是超时原因
        self.last += 1
        #利用变化求和,而不是去遍历
        mid_index = self.last // 2
        new_median = self.array[mid_index]
        delta = abs(new_median - old_median)
        #如果新加入的数不充当中位数, 还要加上新的差值
        if x != new_median and x != old_median:
            self.sum += abs(new_median - x)
        if new_median < old_median:
            self.sum += (self.last - mid_index - 1) * delta - mid_index * delta
        else:
            self.sum += - (self.last - mid_index - 1) * delta + mid_index * delta
    def query(self):
        if not self.last: #此时还没插入过元素
            print(0)
            return
        print(self.sum)
        return 


Q = int(input())
myls = MyList(100010) # 1 <= Q <= 10**5

for i in range(Q):
    oper = list(map(int, input().split()))
    if oper[0] == 1:
        myls.binarysearch_push(oper[1])
    elif oper[0] == 2:
        myls.query()
