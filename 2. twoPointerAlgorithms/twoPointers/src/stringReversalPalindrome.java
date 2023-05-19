public class stringReversalPalindrome {

    public static void main(String[] args) {

        String strValue = "racecar";
        System.out.println(strValue + " is palindrome ?: "+checkIfPalindrome(strValue));

    }




    // check if string is palindrome -- using two pinter technique
    public static boolean checkIfPalindrome(String s) {
        int leftPointer = 0;
        int rightPointer = s.length() - 1;

        while (leftPointer < rightPointer) {
            if (s.charAt(leftPointer) != s.charAt(rightPointer)) {
                return false;
            }
            leftPointer++;
            rightPointer--;
        }

        return true;
    }
}
