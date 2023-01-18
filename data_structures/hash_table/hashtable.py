from typing import NamedTuple, Any

BLANK = object()

class Pair(NamedTuple):
	"""
		- Any: any data type
		- extend NamedTuple parent to let your class inherits all regular tuple's behaviors
	"""
	key: Any
	value: Any

"""
Define a Custom HashTable Class
"""
class HashTable:
	def __init__(self, capacity):
		# self.capacity = capacity
		# self.pairs = capacity * [None]
		# self.pairs = capacity * [BLANK]
		# self._slots = capacity * [None]
		if capacity < 1:
			raise ValueError("Capacity must be a positive number")
		self._slots = capacity * [None]

	def __len__(self):
		# return len(self.pairs)
		# return len(self._slots)
		return len(self.pairs)

	"""
	Insert a Key-Value Pair
	"""
	def __setitem__(self, key, value):
		# # # # self.pairs.append(value) # ignores the key, and the length will increase
		# # # index = hash(key) % len(self)
		# # # """
		# # # 	hash(): turn an arbitary key into a numeric hash value
		# # # 	%: to constrain the resulting index within the available address space

		# # # 	hash code collisions, PYTHONHASHSEED
		# # # """
		# # # self.pairs[index] = value
		# # # self.pairs[self._index(key)] = value
		# # self.pairs[self._index(key)] = (key, value)
		# self.pairs[self._index(key)] = Pair(key, value)
		self._slots[self._index(key)] = Pair(key, value)

	"""
	Find a Value by Key
	"""
	def __getitem__(self, key):
		# # index = hash(key) % len(self)
		# # value = self.pairs[index]
		# value = self.pairs[self._index(key)]
		# if value is BLANK:
		# 	"""
		# 		is: compare identites
		# 		==: compare pairs
		# 	"""
		# 	raise KeyError(key)
		# return value
		# pair = self.pairs[self._index(key)]
		pair = self._slots[self._index(key)]
		if pair is None:
			raise KeyError(key)
		# return pair[1]
		return pair.value

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
		# # # del self.pairs[index]  # the length will decrease
		# # self.pairs[index] = BLANK
		# self.pairs[self._index(key)] = BLANK

		# Assigning a value through the square brackets syntax delegates to the .__setitem__() method
		if key in self:
			# self[key] = BLANK
			# self.pairs[self._index(key)] = None
			self._slots[self._index(key)] = None
			"""
			- You can't use brackets syntax because this would result in wrapping whatever sentinel value you chose in an unnecessary tuple.
			- You must use an explicit assignment statement here to avoid needlessly complicated logic down the road.
			"""
		else:
			raise KeyError(key)

	def _index(self, key):
		# # return hash(key) % len(self)
		# return hash(key) % len(self._slots)
		return hash(key) % self.capacity

	"""
	Update the Value of an Existing Pair
		- the insert method should already take care of updating a key-value pair
	"""

	"""
	Get the Key-Value Pairs
		- refactoring
		- Use Defensive Copying
		- white box testing
		- Get the Keys and Values
	"""
	@property
	def pairs(self):
		# # return self._slots.copy()
		# return [pair for pair in self._slots if pair]
		return {pair for pair in self._slots if pair}

	@property
	def values(self):
		return [pair.value for pair in self.pairs]

	@property
	def keys(self):
		return {pair.key for pair in self.pairs}

	"""
	Report the Hash Table's Length
	"""
	@property
	def capacity(self):
		return len(self._slots)