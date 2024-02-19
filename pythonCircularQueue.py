class Queue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.front = 0
        self.rear = -1
        self.size = 0
        self.items = [None]*maxSize
    
    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.maxSize
    
    def enqueue(self, newItem):
        if self.isFull():
            print("The queue is full")
        else:
            self.rear = (self.rear + 1) % self.maxSize
            self.size += 1
            self.items[self.rear] = newItem
            
    def dequeue(self):
        if self.isEmpty():
            print("The Queue is empty")
        else:
            self.firstItem = self.items[self.front]
            self.front = (self.front + 1)%self.maxSize
            self.size -= 1
            return self.firstItem
