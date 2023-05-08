class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# Stack - Array implementation
class Stack():
    def __init__(self):
        self.array = []
        
    def __str__(self):
        return str(self.__dict__)
        
    def peek(self):
        return self.array[len(self.array)-1]
        
    def push(self, value):
        self.array.append(value)
        return self
        
    def pop(self):
        self.array.pop()
        return self

# Stack - Linked List implementation
class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
        
    def __str__(self):
        return str(self.__dict__)
    
    def peek(self):
        return self.top.value
        
    def push(self, value):
        new_node = Node(value)
        if self.top == None:
            self.bottom = new_node
            self.top = self.bottom
            self.length = 1
        else:
            holding = self.top
            self.top = new_node
            self.top.next = holding
            self.length += 1
            
    def pop(self):
        if not self.top:
            return None
        if self.top == self.bottom:
            self.bottom = None
        self.top = self.top.next
        self.length -= 1
        return self
    
    def printlist(self):
        myarr = []
        currentNode = self.top
        while currentNode != None:
            myarr.append(currentNode.value)
            currentNode = currentNode.next
        return myarr
        
stack = Stack()
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.pop()
stack.pop()
print(stack.printlist())
print(stack.peek())
