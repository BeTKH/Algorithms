import java.util.*;

public class combineSortedLists {

    public static void main(String[] args) {

        int[] arry_1 = {1, 4, 7, 20};
        int[] arry_2 = {3, 5, 6};

        List<Integer> combined_arr = combine(arry_1, arry_2);
        System.out.println(combined_arr);

    }

    public static List<Integer> combine(int[] arr1, int[] arr2) {
        List<Integer> ans = new ArrayList<>();
        int i = 0;
        int j = 0;

        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] < arr2[j]) {
                ans.add(arr1[i]);
                i++;
            } else {
                ans.add(arr2[j]);
                j++;
            }
        }

        while (i < arr1.length) {
            ans.add(arr1[i]);
            i++;
        }

        while (j < arr2.length) {
            ans.add(arr2[j]);
            j++;
        }

        return ans;
    }

}
