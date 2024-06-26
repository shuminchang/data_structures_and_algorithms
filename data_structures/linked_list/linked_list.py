class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)
        
    def add(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)
        if index >= self.length:
            self.add(value)
            return
        if index == 0:
            self.prepend(value)
            return
        leading = self.traverseToIndex(index-1)
        holding = leading.next
        leading.next = new_node
        new_node.next = holding
        self.length += 1
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        elif index == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
        else:
            leading = self.traverseToIndex(index-1)
            unwant = leading.next
            leading.next = unwant.next
            if index == self.length - 1:
                self.tail = leading
        self.length -= 1
        
    def reverse(self):
        prev = None
        currentNode = self.head
        self.tail = currentNode
        while currentNode:
            n = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = n
        self.head = prev
        
    def traverseToIndex(self, index):
        count = 0
        currentNode = self.head
        while count != index:
            currentNode = currentNode.next
            count += 1
        return currentNode
        
    def printlist(self):
        myarr = []
        currentNode = self.head
        while currentNode:
            myarr.append(currentNode.value)
            currentNode = currentNode.next
        return myarr
        
mylist = LinkedList()
mylist.prepend(888)
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.prepend(99)
mylist.insert(99, 88)
mylist.insert(0, 88)
mylist.insert(4, 88)
print(mylist.printlist())
mylist.remove(88)
print(mylist.printlist())
mylist.remove(0)
print(mylist.printlist())
mylist.remove(3)
print(mylist.printlist())
mylist.reverse()
print(mylist.printlist())
