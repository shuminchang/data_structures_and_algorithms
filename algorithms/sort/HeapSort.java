public class HeapSort {

    public static void heapify(int[] arr, int n, int i) {
        int largest = i;
        int leftChild = 2 * i + 1;
        int rightChild = 2 * i + 2;

        // Check if left child exists and is greater than the root
        if (leftChild < n && arr[leftChild] > arr[largest]) {
            largest = leftChild;
        }

        // Check if right child exists and is greater than the root or left child
        if (rightChild < n && arr[rightChild] > arr[largest]) {
            largest = rightChild;
        }

        // Swap the root if necessary
        if (largest != i) {
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;
            // Recursively heapify the affected sub-tree
            heapify(arr, n, largest);
        }
    }

    public static void heapSort(int[] arr) {
        int n = arr.length;

        // Build a max-heap (rearrange array)
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        // Extract elements from the heap one by one
        for (int i = n - 1; i > 0; i--) {
            // Swap root with the last element
            int temp = arr[i];
            arr[i] = arr[0];
            arr[0] = temp;
            // Heapify the reduced heap
            heapify(arr, i, 0);
        }
    }

    public static void main(String[] args) {
        int[] inputArray = {12, 11, 13, 5, 6, 7};
        heapSort(inputArray);
        System.out.println("Sorted array: " + inputArray.toString());
        for (int num : inputArray) {
            System.out.println(num + " ");
        }
    }
}
