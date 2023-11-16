def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if left child exists and is greater than the root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if right child exists and is greater than the root or left child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Swap the root if necessary
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max-heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

# Example usage
if __name__ == "__main__":
    input_list = [12, 11, 13, 5, 6, 7]
    heap_sort(input_list)
    print("Sorted array:", input_list)
