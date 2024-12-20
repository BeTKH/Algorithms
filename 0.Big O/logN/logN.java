public class logN{

    // O(log n) time complexity

    public static void main(String [] args) {


        // binary search
        int[] numbers = {1, 3, 5, 7, 9, 11, 13, 15};
        int target = 9;
        int serachIndex = binarySearch(numbers, target);
        System.out.println("the index of searched target item is: "+serachIndex);



        // exponentiation

        int base = 2;
        int exponent = 10;
        int result = power(base, exponent);
        System.out.println(base + " raised to the power of " + exponent + " is: " + result);



        // GCD
        int a = 24;
        int b = 18;

        int gcd = findGCD(a, b);
        System.out.println("GCD of " + a + " and " + b + " is: " + gcd);



        // Divide and conquer algorithms - quick sort


    }








    // binary search
    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1; // Element not found
    }




    // exponentiation
    public static int power(int base, int exponent) {
        if (exponent == 0) {
            return 1;
        } else if (exponent % 2 == 0) {
            int halfPower = power(base, exponent / 2);
            return halfPower * halfPower;
        } else {
            int halfPower = power(base, exponent / 2);
            return halfPower * halfPower * base;
        }
    }


    // GCD finder
    public static int findGCD(int a, int b) {
        if (b == 0) {
            return a;
        }
        return findGCD(b, a % b);
    }
}
