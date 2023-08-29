class BinarySearch {
    public static int binarySearch(int[] array, int x) {
        int left = 0;
        int right = array.length - 1;
        
        while (right >= left) {
            int mid = left + (right - left) / 2;
            if (x > array[mid]) {
                left = mid + 1;
            } else if (x < array[mid]) {
                right = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
    
    public static void main(String args[]) {
        BinarySearch ob = new BinarySearch();
        int array[] = { 1, 2, 3, 4, 5};
        int x = 5;
        
        int result = ob.binarySearch(array, x);
        
        if (result == -1) {
            System.out.println("Element not found");
        } else {
            System.out.println("Element found at index: " + result);
        }
    }
}
