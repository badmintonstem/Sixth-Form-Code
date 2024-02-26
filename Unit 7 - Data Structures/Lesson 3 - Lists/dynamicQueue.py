class DynamicQueue:
    def __init__(self, maxSize=None):
        self.items = []
        self.maxSize = maxSize
    
    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.maxSize

    def enqueue(self, newItem):
        if self.isFull():
            print("Queue is full")
        else:
            self.items.append(newItem)
            
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.items.pop(0)
   
myToDoList = DynamicQueue(3)
print(myToDoList.isEmpty())
print(myToDoList.isFull())
myToDoList.enqueue("Dishes")
myToDoList.enqueue("Cooking")
print(myToDoList.isEmpty())
print(myToDoList.isFull())
myToDoList.enqueue("Shoping")
myToDoList.enqueue("Watch TV")
print(myToDoList.dequeue())
print(myToDoList.dequeue())
print(myToDoList.dequeue())
print(myToDoList.dequeue())
print(myToDoList.dequeue())