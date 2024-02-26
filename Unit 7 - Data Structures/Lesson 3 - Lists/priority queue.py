#OCR A Level Computer Science
#Unit 7 Data Structures Topic 3 Lists and linked lists
#program priority queue.py implements a priority queue
#as a dynamic list

#Author: PG Online team
#Date: 14/04/2016

#constructing a queue ADT
class Queue:
    def __init__(self):
 #       self.priorityQueue = [[1,'job 1'],[2,'job2'],[2,'job12']]
        self.priorityQueue = []    

        
    def enqueue(self, item):
# put the new item temporarily at the end of the queue
#this ensures there is one item in the queue, items[0]
        self.priorityQueue.append(item)
        index = 0

# now compare the priority number (1 = High, 2 = Medium etc) of the new item
# with each item in list of items, starting at items[0]
#stop when the priority number is greater than the current item
# this means the priority is less, as High Priority = 1, medium = 2 etc
# count the number of items with lower priority, store in index
        while (item[0] >= self.priorityQueue[index][0])   \
                        & (index < len(self.priorityQueue)-1):
            index+=1

        pos = len(self.priorityQueue) - 1
        
# now start from the end of the queue
# and shift all the items along the list
# to where the new item will go
        for count in range(len(self.priorityQueue) - index - 1):
#            print("count =",count)
            self.priorityQueue[pos] = self.priorityQueue[pos-1]
            pos -= 1

# now store the item in the correct place
        self.priorityQueue[index] = item
        print (self.priorityQueue)
#ENDSUB enqueue
    
    def dequeue(self):
        if len(self.priorityQueue) > 0:
            return self.priorityQueue.pop(0)
        else:
            return "Queue empty"
        
    def size(self):
        return len(self.priorityQueue)
    
    def show(self):
        print(self.priorityQueue)
     
    def showFront(self):
        print(self.priorityQueue[0])
        
    def showRear(self):
        print (self.priorityQueue[len(self) -1])
        
q = Queue()


q.enqueue([3,'job13'])
q.enqueue([3,'job14'])
q.enqueue([1,'job1'])
q.enqueue([2,'job2'])
q.enqueue([3,'job18'])
q.enqueue([1,'job10'])
q.enqueue([2,'job20'])
q.enqueue([1,'job100'])
print("\nFinal Queue")
q.show()