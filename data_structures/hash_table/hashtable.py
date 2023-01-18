class HashTable:
	def __init__(self, capacity):
		# self.capacity = capacity
		self.values = capacity * [None]

	def __len__(self):
		return len(self.values)