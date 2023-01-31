class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def add(self, data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			self.tail = self.head
			self.length = 1
		else:
			self.tail.next = new_node
			self.tail = new_node
			self.length += 1

	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		self.length += 1

	def insert(self, index, data):
		new_node = Node(data)
		if index >= self.length:
			self.add(data)
			return
		if index == 0:
			self.prepend(data)
			return
		leading = self.traverseToIndex(index-1)
		holdingPointer = leading.next
		new_node.next = holdingPointer
		leading.next = new_node
		self.length += 1

	def remove(self, index):
		if index >= self.length:
			leading = self.traverseToIndex(self.length - 2)
			# unwant = leading.next
			# leading.next = unwant.next
			leading.next = self.tail.next
			self.tail = leading
			self.length -= 1
		elif index == 0:
			self.head = self.head.next
			self.length -= 1
		else:
			leading = self.traverseToIndex(index - 1)
			unwant = leading.next
			leading.next = unwant.next
			self.length -= 1

	def reverse(self):
		prev = None
		currentNode = self.head
		while currentNode:
			n = currentNode.next
			currentNode.next = prev
			prev = currentNode
			currentNode = n
		self.head = prev

	def size(self):
		return self.length

	def traverseToIndex(self, index):
		counter = 0
		currentNode = self.head
		while counter != index: # can't be counter <= index, why?
			currentNode = currentNode.next
			counter += 1
		return currentNode
	
	def printlist(self):
		arr = []
		currentNode = self.head
		while currentNode != None:
			arr.append(currentNode.data)
			currentNode = currentNode.next
		return arr

mylist = LinkedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.prepend(99)
mylist.insert(99, 88)
mylist.insert(0, 88)
mylist.insert(3, 88)
print(mylist.printlist(), mylist.size())
print(mylist.head.data, mylist.tail.data)
mylist.remove(88)
print(mylist.printlist(), mylist.size())
print(mylist.head.data, mylist.tail.data)
mylist.remove(0)
print(mylist.printlist(), mylist.size())
print(mylist.head.data, mylist.tail.data)
mylist.remove(2)
print(mylist.printlist(), mylist.size())
print(mylist.head.data, mylist.tail.data)
mylist.reverse()
print(mylist.printlist(), mylist.size())
print(mylist.head.data, mylist.tail.data)