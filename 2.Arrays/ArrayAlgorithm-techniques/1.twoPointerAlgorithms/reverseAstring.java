import java.util.Arrays;

public class reverseAstring {

    public static void main(String[] args) {

        char[] string_ = {'h','e','l','l','o'};

        reverseString(string_);


    }


    public static void reverseString(char[] stringInput_) {

        // create two pointers: one at the beginning and one at the end of the array
        int leftPointer = 0;
        int rightPointer = stringInput_.length - 1;

        // loop through the array, swapping the characters at the two pointers
        while (leftPointer < rightPointer) {


            char tempCharacter = stringInput_[leftPointer];

            stringInput_[leftPointer] = stringInput_[rightPointer];
            stringInput_[rightPointer] = tempCharacter;

            leftPointer++;
            rightPointer--;
        }


        System.out.println(Arrays.toString(stringInput_));

    }
}
