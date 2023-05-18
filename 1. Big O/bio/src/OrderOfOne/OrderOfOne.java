package OrderOfOne;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Stack;


// time complexity

public class OrderOfOne {

    public static void main(String[] args) {

        // indexing an array O(1)
        int[] arry = {1,2,3,4,5};
        System.out.println(arry[1]);

        // Inserting or deleting an element at the beginning or end of a linked list:
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.addFirst(10); // Insert at the beginning
        linkedList.addLast(20); // Insert at the end
        int removedElement = linkedList.removeFirst(); // Remove from the beginning
        System.out.println("Removed element: " + removedElement);


        // Pushing and popping elements from a stack
        Stack<Integer> stack_ = new Stack<>();
        stack_.push(10);
        stack_.push(20);
        int poppedElement = stack_.pop();
        System.out.println("Popped element: " + poppedElement);

        //Inserting or retrieving elements from a hash table
        HashMap<String, Integer> hashTable_ = new HashMap<>();
        hashTable_.put("apple", 10);
        hashTable_.put("banana", 20);
        int value = hashTable_.get("apple"); // retrieve element
        System.out.println("Value: " + value);

        // Performing arithmetic operations
        int a = 5;
        int b = 3;
        int sum = a + b; // Addition
        int difference = a - b; // Subtraction
        int product = a * b; // Multiplication
        int quotient = a / b; // Division
        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);
        System.out.println("Product: " + product);
        System.out.println("Quotient: " + quotient);

    }
}
