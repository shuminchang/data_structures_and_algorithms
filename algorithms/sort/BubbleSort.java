// Bubble sort in java
import java.util.Arrays;

class Main {
    
    // perform the bubble sort
    static void bubbleSort(int[] array, int size) {
        
        // loop to access each array element
        for (int i = 0; i < size - 1; i++) {
            
            // loop to compare array elements
            for (int j = 0; j < size - i - 1; j++) {
                
                // compare two adjacent elements
                // change > to < to sort in descending order
                if (array[j] > array[j+1]) {
                    
                    // swapping occurs if elements
                    // are not in the intended order
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
    }
    public static void main(String[] args) {
        int[] array = {4, 2, 3, 1, 5};
        int size = array.length;
        bubbleSort(array, size);
        System.out.println(Arrays.toString(array));
    }
}
