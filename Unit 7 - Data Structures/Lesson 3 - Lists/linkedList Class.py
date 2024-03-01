class LinkedList:
    
    class node:
        data = None
        pointer = None
    
    def __init__(self):
        self.start = None
        self.nextFree = 0
    
    def add(self, item):
        new_node = self.node()
        new_node.data = item
        current_node = self.start
        #list is empty
        if current_node == None:
            new_node.pointer = None
            self.start = new_node
        else:
            if item < current_node.data:
                self.start = new_node
                new_node.pointer = current_node
            else:
                while current_node != None and current_node.data<item:
                    previous_node = current_node
                    current_node = current_node.pointer
                new_node.pointer = previous_node.pointer
                previous_node.pointer = new_node
        return True
    def delete(self, item):
        current_node = self.start
        #check if the list is not empty
        if current_node != None:
            #Item is the start node
            if item == current_node.data:
                self.start = current_node.pointer
            else:
                #find the item
                while current_node != None and item != current_node.data:
                    previous = current_node
                    current_node = current_node.pointer
                previous.pointer = current_node.pointer
    
    def output(self):
        items = []
        current_node = self.start
        if current_node != None:
            #Visit each node
            while current_node != None:
                items.append(current_node.data)
                current_node = current_node.pointer
            return items
        
namesList = LinkedList()
namesList.add("Nancy")
print(namesList.output())
namesList.add("Ava")
print(namesList.output())
namesList.add("Dave")
print(namesList.output())
namesList.add("Peter")
print(namesList.output())
