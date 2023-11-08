public class MergeSort {
    public static void mergeSort(int[] arr) {
        if (arr.length <= 1) {
            return;
        }

        int mid = arr.length / 2;
        int[] left = new int[mid];
        int[] right = new int[arr.length - mid];

        // Populate subarrays
        for (int i = 0; i < mid; i++) {
            left[i] = arr[i];
        }

        for (int i = mid; i < arr.length; i++) {
            right[i - mid] = arr[i];
        }

        // Recursive calls to mergeSort for left and right subarrays
        mergeSort(left);
        mergeSort(right);

        // Merge the sorted subarrays
        merge(arr, left, right);
    }

    public static void merge(int[] arr, int[] left, int[] right) {
        int leftIndex = 0;
        int rightIndex = 0;
        int mergedIndex = 0;

        // Compare elements from left and right subarrays and merge them in sorted order
        while (leftIndex < left.length && rightIndex < right.length) {
            if (left[leftIndex] < right[rightIndex]) {
                arr[mergedIndex] = left[leftIndex];
                leftIndex++;
            } else {
                arr[mergedIndex] = right[rightIndex];
                rightIndex++;
            }
            mergedIndex++;
        }

        // Add remaining elements from left subarray, if any
        while (leftIndex < left.length) {
            arr[mergedIndex] = left[leftIndex];
            leftIndex++;
            mergedIndex++;
        }

        // Add remaining elements from right subarray, if any
        while (rightIndex < right.length) {
            arr[mergedIndex] = right[rightIndex];
            rightIndex++;
            mergedIndex++;
        }
    }

    public static void main(String[] args) {
        int[] inputArray = {12, 11, 13, 5, 6, 7};
        mergeSort(inputArray);
        System.out.print("Sorted array: ");
        for (int num : inputArray) {
            System.out.print(num + " ");
        }
    }
}
