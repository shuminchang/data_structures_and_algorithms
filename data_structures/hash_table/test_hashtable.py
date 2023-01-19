from hashtable import HashTable, BLANK
import pytest
from pytest_unordered import unordered

"""
Define a Custom HashTable Class
"""
def test_should_create_hashtable():
	assert HashTable(capacity=100) is not None

def test_shourld_report_capacity():
	assert len(HashTable(capacity=100)) == 0

def test_should_create_empty_value_slots():
	# Given
	expected_slots = [None, None, None]
	# expected_slots = [BLANK, BLANK, BLANK]
	hash_table = HashTable(capacity=3)

	# When
	# actual_slots = hash_table.pairs
	actual_slots = hash_table._slots

	# Then
	assert actual_slots == expected_slots

"""
Insert a Key-Value Pair
"""
def test_should_insert_key_value_slots():
	hash_table = HashTable(capacity=100)

	hash_table["hola"] = "hello"
	hash_table[98.6] = 37
	hash_table[False] = True

	assert ("hola", "hello") in hash_table.pairs
	assert (98.6, 37) in hash_table.pairs
	assert (False, True) in hash_table.pairs

	assert len(hash_table) == 3

@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
	pass

def test_should_not_contain_none_value_when_created():
	# # assert None not in HashTable(capacity=100).pairs
	# hash_table = HashTable(capacity=100)
	# values = [pair.value for pair in hash_table.pairs if pair]
	# assert None not in values
	assert None not in HashTable(capacity=100).values

def test_should_insert_none_value():
	# happy path
	hash_table = HashTable(capacity=100)
	hash_table["key"] = None
	assert ("key", None) in hash_table.pairs

"""
Find a Value by Key
"""
@pytest.fixture
def hash_table():
	hash_table = HashTable(capacity=100)
	hash_table["hola"] = "hello"
	hash_table[98.6] = 37
	hash_table[False] = True
	return hash_table

def test_should_find_value_by_key(hash_table):
	assert hash_table["hola"] == "hello"
	assert hash_table[98.6] == 37
	assert hash_table[False] is True

def test_should_raise_error_on_missing_key():
	hash_table = HashTable(capacity=100)
	with pytest.raises(KeyError) as exception_info:
		hash_table["missing_key"]
	assert exception_info.value.args[0] == "missing_key"

def test_should_find_key(hash_table):
	assert "hola" in hash_table

def test_should_not_find_key(hash_table):
	assert "missing_key" not in hash_table

def test_should_get_value(hash_table):
	assert hash_table.get("hola") == "hello"

def test_should_get_none_when_missing_key(hash_table):
	assert hash_table.get("missing_key") is None

def test_should_get_default_value_when_missing_key(hash_table):
	assert hash_table.get("missing_key", "default") == "default"

def test_should_get_value_with_default(hash_table):
	assert hash_table.get("hola", "default") == "hello"

"""
Delete a Key-Value Pair
"""
def test_should_delete_key_value_pair(hash_table):
	assert "hola" in hash_table
	assert ("hola", "hello") in hash_table.pairs
	assert len(hash_table) == 3

	del hash_table["hola"]

	assert "hola" not in hash_table
	assert ("hola", "hello") not in hash_table.pairs
	assert len(hash_table) == 2

def test_should_raise_key_error_when_deleting(hash_table):
	with pytest.raises(KeyError) as exception_info:
		del hash_table["missing_key"]
	assert exception_info.value.args[0] == "missing_key"

"""
Update the Value of an Existing Pair
	- the insert method should already take care of updating a key-value pair, just add a relevant test case
"""
def test_should_update_value(hash_table):
	assert hash_table["hola"] == "hello"

	hash_table["hola"] = "hallo"

	assert hash_table["hola"] == "hallo"
	assert hash_table[98.6] == 37
	assert hash_table[False] == True
	assert len(hash_table) == 3

"""
Get the Key-Value Pairs
	- refactoring
	- Use Defensive Copying
"""
def test_should_return_slots(hash_table):
	assert ("hola", "hello") in hash_table.pairs
	assert (98.6, 37) in hash_table.pairs
	assert (False, True) in hash_table.pairs

def test_should_return_copy_of_slots(hash_table):
	assert hash_table.pairs is not hash_table.pairs

def test_should_not_include_blank_slots(hash_table):
	assert None not in hash_table.pairs

def test_should_return_duplicate_values():
	hash_table = HashTable(capacity=100)
	hash_table["Alice"] = 24
	hash_table["Bob"] = 42
	hash_table["Joe"] = 42
	assert [24, 42, 42] == sorted(hash_table.values)

def test_should_get_values(hash_table):
	assert unordered(hash_table.values) == ["hello", 37, True]

def test_should_get_values_of_empty_hash_table():
	assert HashTable(capacity=100).values == []

def test_should_return_copy_of_values(hash_table):
	assert hash_table.values is not hash_table.values

def test_should_get_keys(hash_table):
	assert hash_table.keys == {"hola", 98.6, False}

def test_should_get_keys_of_empty_hash_table():
	assert HashTable(capacity=100).keys == set()

def test_should_return_copy_of_keys(hash_table):
	assert hash_table.keys is not hash_table.keys

def test_should_return_slots(hash_table):
	assert hash_table.pairs == {
		("hola", "hello"),
		(98.6, 37),
		(False, True)
	}

def test_should_get_slots_of_empty_hash_table():
	assert HashTable(capacity=100).pairs == set()

def test_should_convert_to_dict(hash_table):
	dictionary = dict(hash_table.pairs)
	assert set(dictionary.keys()) == hash_table.keys
	assert set(dictionary.items()) == hash_table.pairs
	assert list(dictionary.values()) == unordered(hash_table.values)

"""
Report the Hash Table's Length
"""
def test_should_report_length_of_empty_hash_table():
	assert len(HashTable(capacity=100)) == 0

def test_should_not_create_hashtable_with_zero_capacity():
	with pytest.raises(ValueError):
		HashTable(capacity=0)

def test_should_not_create_hashtable_with_negative_capacity():
	with pytest.raises(ValueError):
		HashTable(capacity=-100)

def test_should_report_length(hash_table):
	assert len(hash_table) == 3

def test_should_report_capacity_of_empty_hash_table():
	assert HashTable(capacity=100).capacity == 100

def test_should_report_capacity(hash_table):
	assert hash_table.capacity == 100

def test_should_create_empty_pair_slots():
	assert HashTable(capacity=3)._slots == [None, None, None]

"""
Make the Hash Table Iterable
	- keys, values, pairs are implemented by sets and lists which can handle iteration
"""
def test_should_iterate_over_keys(hash_table):
	for key in hash_table.keys:
		assert key in ("hola", 98.6, False)

def test_should_iterate_over_values(hash_table):
	for value in hash_table.values:
		assert value in ("hello", 37, True)

def test_should_iterate_over_pairs(hash_table):
	for key, value in hash_table.pairs:
		assert key in hash_table.keys
		assert value in hash_table.values

# When you want to iterate instance of hashtable class, you need generator iterator
def test_should_iterate_over_instance(hash_table):
	for key in hash_table:
		assert key in ("hola", 98.6, False)