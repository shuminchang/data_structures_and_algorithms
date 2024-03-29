def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        
        mid = (left + right) // 2

        if x < arr[mid]:
            right = mid - 1
        elif x > arr[mid]:
            left = mid + 1
        else:
            return mid
    return False
    
arry = [1, 2, 3, 4, 5]
x = 5
print(binary_search(arry, x))
