// Program to calculate the product of three integers
import java.util.Scanner; // program uses class Scanner

public class ProductOfThreeIntegers {
   // main method begins execution of Java application
   public static void main(String[] args) {
      // a) State that a program will calculate the product of three integers
      System.out.println("This program will calculate the product of three integers.");

      // b) Create a Scanner called input that reads values from the standard input
      Scanner input = new Scanner(System.in);

      // c) Prompt the user to enter the first integer
      System.out.print("Enter the first integer: ");
      // d) Read the first integer from the user and store it in the int variable x
      int x = input.nextInt();

      // e) Prompt the user to enter the second integer
      System.out.print("Enter the second integer: ");
      // f) Read the second integer from the user and store it in the int variable y
      int y = input.nextInt();

      // g) Prompt the user to enter the third integer
      System.out.print("Enter the third integer: ");
      // h) Read the third integer from the user and store it in the int variable z
      int z = input.nextInt();

      // i) Compute the product of the three integers contained in variables x, y, and z, and store the result in the int variable result
      int result = x * y * z;

      // j) Use System.out.printf to display the message "Product is" followed by the value of the variable result
      System.out.printf("Product is %d%n", result);
   } // end method main
} // end class ProductOfThreeIntegers
