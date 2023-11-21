def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        current_value = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > current_value:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = current_value
    return bucket

def bucket_sort(arr):
    if not arr:
        return arr

    # Find the maximum and minimum values in the input array
    max_val = max(arr)
    min_val = min(arr)

    # Ensure there is at least one bucket
    if max_val == min_val:
        return arr

    # Calculate the range of each bucket
    bucket_range = max_val - min_val

    # Create empty buckets
    buckets = [[] for _ in range(len(arr))]

    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) // bucket_range * len(arr) - 1)
        buckets[index].append(num)

    # Sort each bucket (using another sorting algorithm, e.g., insertion sort)
    for i in range(len(buckets)):
        buckets[i] = insertion_sort(buckets[i])

    # Concatenate the sorted buckets to get the final sorted array
    sorted_arr = [num for bucket in buckets for num in bucket]

    return sorted_arr

# Example usage
arr = [4, 2, 7, 1, 0.3, 9, 5, 8, -0.6]
sorted_arr = bucket_sort(arr)
print("Original array:", arr)
print("Sorted array:", sorted_arr)
