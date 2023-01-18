BLANK = object()

class HashTable:
	def __init__(self, capacity):
		# self.capacity = capacity
		# self.values = capacity * [None]
		self.values = capacity * [BLANK]

	def __len__(self):
		return len(self.values)

	def __setitem__(self, key, value):
		# self.values.append(value) # ignores the key, and the length will increase
		index = hash(key) % len(self)
		"""
			hash(): turn an arbitary key into a numeric hash value
			%: to constrain the resulting index within the available address space

			hash code collisions, PYTHONHASHSEED
		"""
		self.values[index] = value

	def __getitem__(self, key):
		index = hash(key) % len(self)
		value = self.values[index]
		if value is BLANK:
			"""
				is: compare identites
				==: compare values
			"""
			raise KeyError(key)
		return value

	def __contains__(self, key):
		try:
			self[key]
		except KeyError as e:
			return False
		else:
			return True

	def get(self, key, default=None):
		try:
			return self[key]
		except:
			return default