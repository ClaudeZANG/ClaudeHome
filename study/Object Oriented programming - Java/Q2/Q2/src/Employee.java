public class Employee {
   private String firstName; // instance variable
   private String lastName; // instance variable
   private double salary; // instance variable

   // Constructor
   public Employee(String firstName, String lastName, double salary) {
      this.firstName = firstName;
      this.lastName = lastName;
      if (salary > 0) { // validate that the salary is positive
         this.salary = salary;
      }
   }

   // Get method for firstName
   public String getFirstName() {
      return firstName;
   }

   // Set method for firstName
   public void setFirstName(String firstName) {
      this.firstName = firstName;
   }

   // Get method for lastName
   public String getLastName() {
      return lastName;
   }

   // Set method for lastName
   public void setLastName(String lastName) {
      this.lastName = lastName;
   }

   // Get method for salary
   public double getSalary() {
      return salary;
   }

   // Set method for salary
   public void setSalary(double salary) {
      if (salary > 0) { // validate that the salary is positive
         this.salary = salary;
      }
   }

   // Method to give a 10% raise
   public void giveRaise() {
      salary = salary * 1.10;
   }
}
