import ctypes
class DynamicArray(object):
    """
    DYNAMIC ARRAY CLASS (Similar to Python List)
    """
    
    def __init__(self):
        self.n = 0 # Count actual elements (default is 0)
        self.capacity = 1 # Default capacity
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        """
        Return number of elements stored in array
        """
        return self.n
        
    def __getitem__(self, k):
        """
        Return element at index k
        """
        if not 0 <= k < self.n:
            # Check it k index is in bounds of array
            return IndexError("k is out of bounds !")
            
        return self.A[k] # Retrieve element from the array at index k
        
    def append(self, ele):
        """
        Add element to end of the array
        """
        if self.n == self.capacity:
            # Double capacity if not enough room
            self._resize(2 * self.capacity)
            
        self.A[self.n] = ele # Set self.n index to element
        self.n += 1
        
    def insertAt(self, item, index):
        """
        This function inserts the item at any specified index.
        """
        
        if index < 0 or index > self.n:
            print("please enter appropriate index.")
            return
        
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
            
        self.A[index] = item
        self.n += 1
        
    def delete(self):
        """
        This function deletes item from the end of array
        """
        if self.n == 0:
            print("Array is empty, deletion not possible")
            return
        
        self.A[self.n - 1] = 0
        self.n -= 1
        
    def removeAt(self, index):
        """
        This function removes item from array at specified index
        """
        if self.n == 0:
            print("Array is empty deletion not possible")
            return
        
        if index < 0 or index > self.n:
            return IndexError("Index out of bound....deletion not possible")
            
        if index == self.n - 1:
            self.A[index] = 0
            self.n -= 1
            
        # Turn elements into their previous item, then remove the last
        for i in range(index, self.n - 1):
            self.A[i] = self.A[i + 1]
            
        self.A[self.n - 1] = 0
        self.n -= 1
        
    def _resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """
        
        B = self.make_array(new_cap) # New bigger array
        
        for k in range(self.n):
            # Reference all existing elements
            B[k] = self.A[k]
            
        self.A = B
        self.capacity = new_cap
        
    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()
        

