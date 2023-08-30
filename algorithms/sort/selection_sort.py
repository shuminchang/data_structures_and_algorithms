# Selection sort python
def selection_sort(array, size):
    for step in range(size):
        min_index = step
        
        for i in range(step + 1, size):
            
            # to sort in descending order, change > to < this line
            # selection the minimum element in each loop
            if array[min_index] > array[i] :
                min_index = i
        
        # put min at the correction position
        temp = array[step]
        array[step] = array[min_index]
        array[min_index] = temp
        
data = [-2, 45, 0, 11, -9]
size = len(data)
selection_sort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
