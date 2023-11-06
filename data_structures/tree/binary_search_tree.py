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
					
	def insert_recursive(self, value):
		self.root = self._insert_recursive(self.root, value)
		
	def _insert_recursive(self, node, value):
		if node is None:
			return Node(value)
		if value < node.value:
			node.left = self._insert_recursive(node.left, value)
		elif value > node.value:
			node.right = self._insert_recursive(node.right, value)
		return node
	
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
	
	def deleteNode(self, value):
		self.root = self._deleteNode(self.root, value)
		
	def _deleteNode(self, root, value):
		if root is None:
			return root
		if value < root.value:
			root.left = self._deleteNode(root.left, value)
		elif value > root.value:
			root.right = self._deleteNode(root.right, value)
		else:  # why else?
			if root.left is None:
				temp = root.right
				root = None
				return temp
			elif root.right is None:
				temp = root.left
				root = None
				return temp
			temp = self.minValueNode(root.right)
			root.value = temp.value
			root.right = self._deleteNode(root.right, temp.value)
		return root
		
	def print_tree(self):
		if self.root != None:
			self.printt(self.root)
			
	def printt(self, curr_node):
		if curr_node != None:
			self.printt(curr_node.left)
			print(str(curr_node.value))
			self.printt(curr_node.right)
			
	def minValueNode(self, node):
		current = node
		while current.left is not None:
			current = current.left
		return current
			
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

tree = BinarySearchTree()
tree.insert_recursive(8)
tree.insert_recursive(3)
tree.insert_recursive(1)
tree.insert_recursive(6)
tree.insert_recursive(7)
tree.insert_recursive(10)
tree.insert_recursive(14)
tree.insert_recursive(4)
tree.deleteNode(3)
print(tree.breadthFirstSearch())