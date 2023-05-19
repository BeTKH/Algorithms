/**
 * Given a sorted array of unique integers and a target integer,
 * return true if there exists a pair of numbers that sum to target,
 * false otherwise
 * */
public class toTarget {

    public static void main(String[] args) {

        int[] nums = {1, 2, 4, 6, 8, 9, 14, 15};
        int target = 13;

        System.out.println(target +": sums in the array nums ?: "+toTarg(nums, target));
    }


    private static boolean toTarg(int[] arry_, int targ_){

        int leftPointer = 0;
        int rightPointer = arry_.length - 1;

        while (leftPointer < rightPointer ){

            int currentSum = arry_[leftPointer] + arry_[rightPointer];

            if (currentSum == targ_){
                return true;
            }


            if (currentSum > targ_){
                rightPointer --;
            }else{
                leftPointer ++;}
        }

        return false;
    }

}
