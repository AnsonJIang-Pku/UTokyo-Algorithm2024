#记录代码的优化过程，超时解1
class MyList:
    def __init__(self, size):
        self.last = 0 #待插入元素的位置，也是现在数组中元素的个数
        self.array = [None] * size
    
    def push(self, x: int):
        #应该不会越界
        self.array[self.last] = x
        self.last += 1
    
    def query(self): # O(Q) oper[0] == 2时才执行
        if not self.last: #此时还没插入过元素
            print(0)
            return
        tempArray = self.array[:self.last]
        tempArray.sort() # O(NlogN)
        mid = tempArray[self.last // 2]
        sum = 0
        for i in range(self.last): # O(N)
            sum += abs(mid - tempArray[i])
        print(sum)
        return 


Q = int(input())
myls = MyList(100010) # 1 <= Q <= 10**5

for i in range(Q):
    oper = list(map(int, input().split()))
    if oper[0] == 1:
        myls.push(oper[1])
    elif oper[0] == 2:
        myls.query()
