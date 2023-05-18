package OrderOfNSquared;

import java.util.Arrays;

public class nSquared {

    public static void main(String[] args) {


        // n^2 complexity = 1 loop nested into another
        int[] numb_list = {7, 2, 1};

        // Nested loops iterating over the same collection
        for (int i = 0; i < numb_list.length; i++) {
            for (int j = 0; j < numb_list.length; j++) {
                System.out.println(numb_list[i] + " " + numb_list[j]);
            }
        }

        // Bubble sort
        int[]  sortedArray = bubbleSort(numb_list);
        System.out.println("The sorted array is: "+ Arrays.toString(sortedArray));

}

    public static int[] bubbleSort(int[] arry_){
        // Bubble sort
        for (int i = 0; i < arry_.length - 1; i++) {
            for (int j = 0; j < arry_.length - i - 1; j++) {
                if (arry_[j] > arry_[j + 1]) {
                    // Swap elements if they are in the wrong order
                    int temp = arry_[j];
                    arry_[j] = arry_[j + 1];
                    arry_[j + 1] = temp;
                }
            }
        }

        return  arry_;
    }




}
