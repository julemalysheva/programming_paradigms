package sem06HW;

import java.util.Arrays;

public class BinarySearch {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 5, 6, 8, 9};
        int target = 5;
        int result = binarySearch(numbers, target);
        
        System.out.println("Список: " + Arrays.toString(numbers));
        System.out.println("Ищем элемент: " + target);
        
        if (result != -1) {
            System.out.println("Элемент найден за индексом: " + result);
        } else {
            System.out.println("Элемент не найден в списке.");
        }
    }

    public static int binarySearch(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;
        
        while (start <= end) {
            int mid = (start + end) / 2;
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        
        return -1;
    }
    
}