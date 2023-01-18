BLANK = object()

"""
Define a Custom HashTable Class
"""
class HashTable:
	def __init__(self, capacity):
		# self.capacity = capacity
		# self.values = capacity * [None]
		self.values = capacity * [BLANK]

	def __len__(self):
		return len(self.values)

	"""
	Insert a Key-Value Pair
	"""
	def __setitem__(self, key, value):
		# # self.values.append(value) # ignores the key, and the length will increase
		# index = hash(key) % len(self)
		# """
		# 	hash(): turn an arbitary key into a numeric hash value
		# 	%: to constrain the resulting index within the available address space

		# 	hash code collisions, PYTHONHASHSEED
		# """
		# self.values[index] = value
		self.values[self._index(key)] = value

	"""
	Find a Value by Key
	"""
	def __getitem__(self, key):
		# index = hash(key) % len(self)
		# value = self.values[index]
		value = self.values[self._index(key)]
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

	"""
	Delete a Key-Value Pair
	"""
	def __delitem__(self, key):
		# # index = hash(key) % len(self)
		# # # del self.values[index]  # the length will decrease
		# # self.values[index] = BLANK
		# self.values[self._index(key)] = BLANK

		# Assigning a value through the square brackets syntax delegates to the .__setitem__() method
		if key in self:
			self[key] = BLANK
		else:
			raise KeyError(key)

	def _index(self, key):
		return hash(key) % len(self)