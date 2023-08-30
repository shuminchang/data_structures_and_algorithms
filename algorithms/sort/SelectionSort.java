// Selection sort in Java
import java.util.Arrays;

class Main {
    
    static void selectionSort(int array[], int size) {
        for (int step = 0; step < size; step++) {
            int min_index = step;
            
            // To sort in descending order, change > to <
            // Select the minimum element in each loop
            for (int i = step + 1; i < size; i++) {
                if (array[min_index] > array[i]) {
                    min_index = i;
                }
            }
            
            // put min at the correct position
            int temp = array[step];
            array[step] = array[min_index];
            array[min_index] = temp;
        }
    }
    
    public static void main(String[] args) {
        int array[] = {-2, 45, 0, 11, -9};
        int size = array.length;
        Main.selectionSort(array, size);
        System.out.println(Arrays.toString(array));
    }
}
