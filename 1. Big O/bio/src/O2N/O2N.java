package O2N;

import java.util.ArrayList;
import java.util.List;

public class O2N {

    public static void main(String[] args) {

        int[] nums = {1, 2, 3};


        // generate & print all subsets -- O(2^n) time complexity
        List<List<Integer>> subsets = generateSubsets(nums);
        for (List<Integer> subset: subsets){
            System.out.println(subset);
        }



        // Recursive Fibonacci sequence -- O(2^n) time complexity
        int limit = 10;
        for (int i = 0; i< limit ; i++){
            System.out.println("fibonacci ("+i+"): "+fibonacci(i) + " ");
        }

    }




    // generate subsets __________________________________________________________________________________start

    public static List<List<Integer>>  generateSubsets(int[] arr_){

        List<List<Integer>> subsets = new ArrayList<>();
        backtrack(arr_, 0, new ArrayList<>(), subsets);
        return subsets;
    }

    private static void backtrack(int[] nums, int start, List<Integer> currentSubset, List<List<Integer>> subsets_){

        subsets_.add(new ArrayList<>(currentSubset));

        for (int i = start; i < nums.length; i++){
            currentSubset.add(nums[i]);
            backtrack(nums, i+1, currentSubset, subsets_);
            currentSubset.remove(currentSubset.size()-1);
        }
    }
    // generate subsets __________________________________________________________________________________end




    //recursive  fibonacci__________________________________________________________________________________start
    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
    //recursive  fibonacci__________________________________________________________________________________end


}
