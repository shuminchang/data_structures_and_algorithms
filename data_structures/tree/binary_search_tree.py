class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value
		
class BinarySearchTree:
	def __init__(self):
		self.root = None
		
	def insert(self, value):
		new_node = Node(value)
		if self.root == None:
			self.root = new_node
		else:
			current_node = self.root
			while True:
				if value < current_node.value:
					if not current_node.left:
						current_node.left = new_node
						return
					current_node = current_node.left
				elif value > current_node.value:
					if not current_node.right:
						current_node.right = new_node
						return
					current_node = current_node.right
	
	def lookup(self, value):
		if self.root == None:
			return False
		current_node = self.root
		while current_node:
			if value < current_node.value:
				current_node = current_node.left
			elif value > current_node.value:
				current_node = current_node.right
			else:
				return current_node.value
		return False
		
	def breadthFirstSearch(self):
		arr = []
		queue = [self.root]
		
		while len(queue) > 0:
			current_node = queue[0]
			arr.append(current_node.value)
			del queue[0]
			if current_node.left:
				queue.append(current_node.left)
			if current_node.right:
				queue.append(current_node.right)
		return arr
		
	def print_tree(self):
		if self.root != None:
			self.printt(self.root)
			
	def printt(self, curr_node):
		if curr_node != None:
			self.printt(curr_node.left)
			print(str(curr_node.value))
			self.printt(curr_node.right)
			
bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
print(bst.print_tree())
print(bst.breadthFirstSearch())
