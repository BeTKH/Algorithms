import java.util.Arrays;

public class SquareSortedArry {

    public static void main(String[] args) {

        int[] sortedArray = {-4, -1, 0, 3, 10};

        int[] res = squareSortedArr(sortedArray);
        System.out.println(Arrays.toString(res));

    }


    /**
     * instead of squaring the array and sorting it again which has complexity of O(n) squarring and O(n logn) for sorting
     * we can do this with O(n) taking advantage of already sorted array
     * */

    public static int[] squareSortedArr(int[] arry_){


        // create two pointers
        int left = 0;
        int right = arry_.length - 1;

        // create empty arry and strt filling the arry from the last index n-1
        int[] resultArry = new int[arry_.length];

        for (int i = right; i > -1; i--){

            if (Math.abs(arry_[right]) > Math.abs(arry_[left])){
                resultArry[i] = arry_[right] * arry_[right];
                right --;
            }else{
                resultArry[i] = arry_[left] * arry_[left];
                left ++;
            }

        }

        return resultArry;
    }
}
