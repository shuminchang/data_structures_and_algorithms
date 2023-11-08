def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the input array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursive calls to merge_sort for both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    
    # Compare elements from left and right subarrays and merge them in sorted order
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    # Add remaining elements from left and right subarrays, if any
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    
    return merged

if __name__ == "__main__":
    input_list = [12, 11, 13, 5, 6, 7]
    sorted_list = merge_sort(input_list)
    print("Sorted array:", sorted_list)