// Insertion sort in java
import java.util.Arrays;

class InsertionSort {
    
    void insertionSort(int[] array) {
        
        for (int i = 1; i < array.length; i++) {
            int currentValue = array[i];
            int currentPosition = i;
            
            // compare currentValue with each element on the left of it 
            // until an element smaller than it is found
            while (currentPosition > 0 && currentValue < array[currentPosition - 1]) {
                array[currentPosition] = array[currentPosition - 1];
                currentPosition = currentPosition - 1;
            }
            array[currentPosition] = currentValue;
        }
    }
    public static void main(String[] args) {
        int[] array = {5, 2, -1, 15, -4};
        InsertionSort insertSort = new InsertionSort();
        insertSort.insertionSort(array);
        System.out.println(Arrays.toString(array));
    }
}
