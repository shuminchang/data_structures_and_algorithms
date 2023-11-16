import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class BucketSort {

    public static List<Integer> insertionSort(List<Integer> bucket) {
        for (int i = 1; i < bucket.size(); i++) {
            int currentValue = bucket.get(i);
            int j = i - 1;
            while (j >= 0 && bucket.get(j) > currentValue) {
                bucket.set(j + 1, bucket.get(j));
                j--;
            }
            bucket.set(j + 1, currentValue);
        }
        return bucket;
    }

    public static List<Integer> bucketSort(List<Integer> arr) {
        if (arr == null || arr.isEmpty()) {
            return arr;
        }

        // Find the maximum and minimum values in the input array
        int maxVal = Collections.max(arr);
        int minVal = Collections.min(arr);

        // Ensure there is at least one bucket
        if (maxVal == minVal) {
            return arr;
        }

        // Calculate the range of each bucket
        int bucketRange = Math.max(1, (maxVal - minVal) / arr.size());

        // Create empty buckets
        List<List<Integer>> buckets = new ArrayList<>(arr.size());
        for (int i = 0; i < arr.size(); i++) {
            buckets.add(new ArrayList<>());
        }

        // Distribute elements into buckets
        for (int num : arr) {
            int index = Math.min((num - minVal) / bucketRange, buckets.size() - 1);
            buckets.get(index).add(num);
        }

        // Sort each bucket (using another sorting algorithm, e.g., insertion sort)
        for (int i = 0; i < buckets.size(); i++) {
            buckets.set(i, insertionSort(buckets.get(i)));
        }

        // Concatenate the sorted buckets to get the final sorted array
        List<Integer> sortedArr = new ArrayList<>();
        for (List<Integer> bucket : buckets) {
            sortedArr.addAll(bucket);
        }

        return sortedArr;
    }

    public static void main(String[] args) {
        List<Integer> arr = Arrays.asList(4, 2, 7, 1, 3, 9, 5, 8, 6);
        List<Integer> sortedArr = bucketSort(arr);
        System.out.println("Original array: " + arr);
        System.out.println("Sorted array: " + sortedArr);
    }
}
