package OrderOfN;

import java.util.ArrayList;
import java.util.List;

// time complexity

public class OrderN {
    public static void main(String[] args) {

        // O(n) operations - linear complexity

        // 1. looping over an array
        int[] arry_ = {1,2,3,4,5,6,7};
        for (int i = 0; i < arry_.length-1; i++){
            System.out.println("looping over ... index: "+i+" and value is: "+arry_[i]);
        }

        // linear search in arry - looping over array example
        int target_ = 7;
        int indexOfTraget = linearSearch(arry_, target_);
        System.out.println("\nIndex of target is: "+indexOfTraget+"\n");



        //traverse/loop through a collecton of strings
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("mango");
        fruits.add("Kiwi");

        for (String item: fruits){
            System.out.println("items in the colection: "+item);
        }
    }





    // linear search
    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1; // Element not found
    }


}
