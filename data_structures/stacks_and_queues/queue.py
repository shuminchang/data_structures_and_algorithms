class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

# Queue - Linked List implementation
class Queue():
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def __str__(self):
    return str(self.__dict__)

  def printlist(self):
    myarray = []
    currentNode = self.first
    while currentNode:
      myarray.append(currentNode.value)
      currentNode = currentNode.next
    return myarray

  def peek(self):
    return self.first.value

  def enqueue(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.first = new_node
      self.last = new_node
    else:
      self.last.next = new_node
      self.last = new_node
    self.length += 1

  def dequeue(self):
    if not self.first:
      return None
    if self.first == self.last:
      self.last = None
    self.first = self.first.next
    self.length -= 1

queue = Queue()
queue.enqueue("David")
print(queue.printlist())
queue.enqueue("Jimmy")
print(queue.printlist())
queue.enqueue("Mary")
print(queue.printlist())
queue.dequeue()
print(queue.printlist())
print(queue.peek())
