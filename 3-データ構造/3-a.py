# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/174318
class Ring_Queue:
    def __init__(self, size: int):
        self.queue = [None] * (size + 1) #为了判断空还是满,要多留出一个空位
        self.head = 0
        self.tail = 0
    
    def enqueue(self, a: int):
        if self.head == (self.tail + 1) % len(self.queue):
            print("queue is full")
            return
        self.queue[self.tail] = a
        self.tail += 1
        self.tail %= len(self.queue)
        return 
    
    def dequeue(self):
        if self.head == self.tail:
            print("queue is empty")
            return 
        temp = self.queue[self.head]
        print(temp)
        self.head += 1
        self.head %= len(self.queue)
        return temp
        
Q, K = map(int, input().split())
#initalize the queue
que = Ring_Queue(K)
for i in range(Q):
    oper = list(map(int, input().split()))
    if oper[0] == 1:
        que.enqueue(oper[1])
    elif oper[0] == 2:
        que.dequeue()
