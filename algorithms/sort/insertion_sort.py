# insertion sort in python
def insertion_sort(nums):
    for i in range(1, len(nums)):
        current_value = nums[i]
        current_position = i
        
        while current_position > 0 and nums[current_position - 1] > current_value:
            nums[current_position] = nums[current_position - 1]
            current_position = current_position - 1
        nums[current_position] = current_value
    return nums
    
nums = [3, 7, 2, 5, 1, 9, 0]
x = insertion_sort(nums)
print(x)
