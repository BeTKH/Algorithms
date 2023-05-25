import java.util.Arrays;

public class findLengthOfSubArray {


    /**
     * Example 1: Given an array of positive integers nums and an integer k,
     * find the length of the longest subarray whose sum is less than or equal to k.
     *
     * */

    public static void main(String[] args) {

        int[] array = {3, 1, 2, 7, 4, 2, 1, 1, 5};

        int target = 8;

        int result = lengthOfLongestSubArry(array, target);
        System.out.println("length of the longest sub array is: "+ result);

    }


    public static int lengthOfLongestSubArry(int[] arry_, int sum_){

        int length = 0;

        int left = 0;
        int current = 1;


        for ( int right = 0; right < arry_.length; right ++){

            current += arry_[right];

            while (current > sum_){
                current -= arry_[left];
                left ++;
            }

            length = Math.max(length, right - left + 1);
        }

        return length;
    }
}
