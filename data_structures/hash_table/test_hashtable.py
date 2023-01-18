from hashtable import HashTable, BLANK
import pytest

"""
Define a Custom HashTable Class
"""
def test_should_create_hashtable():
	assert HashTable(capacity=100) is not None

def test_shourld_report_capacity():
	assert len(HashTable(capacity=100)) == 100

def test_should_create_empty_value_slots():
	# Given
	# expected_values = [None, None, None]
	expected_values = [BLANK, BLANK, BLANK]
	hash_table = HashTable(capacity=3)

	# When
	actual_values = hash_table.values

	# Then
	assert actual_values == expected_values

"""
Insert a Key-Value Pair
"""
def test_should_insert_key_value_pairs():
	hash_table = HashTable(capacity=100)

	hash_table["hola"] = "hello"
	hash_table[98.6] = 37
	hash_table[False] = True

	assert "hello" in hash_table.values
	assert 37 in hash_table.values
	assert True in hash_table.values

	assert len(hash_table) == 100

@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
	pass

def test_should_not_contain_none_value_when_created():
	assert None not in HashTable(capacity=100).values

def test_should_insert_none_value():
	# happy path
	hash_table = HashTable(capacity=100)
	hash_table["key"] = None
	assert None in hash_table.values

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
	assert "hello" in hash_table.values
	assert 37 in hash_table.values
	assert True in hash_table.values

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
	assert "hello" in hash_table.values
	assert len(hash_table) == 100

	del hash_table["hola"]

	assert "hola" not in hash_table
	assert "hello" not in hash_table.values
	assert len(hash_table) == 100

def test_should_raise_key_error_when_deleting(hash_table):
	with pytest.raises(KeyError) as exception_info:
		del hash_table["missing_key"]
	assert exception_info.value.args[0] == "missing_key"