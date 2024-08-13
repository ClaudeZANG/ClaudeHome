public class EmployeeTest {
   public static void main(String[] args) {
      // Initialize two Employee objects
      Employee employee1 = new Employee("John", "Doe", 3000);
      Employee employee2 = new Employee("Jane", "Smith", 3500);

      // Display the information of the two employees
      System.out.printf("Employee 1: %s %s, Salary: $%.2f%n",
         employee1.getFirstName(), employee1.getLastName(), employee1.getSalary());
      System.out.printf("Employee 2: %s %s, Salary: $%.2f%n",
         employee2.getFirstName(), employee2.getLastName(), employee2.getSalary());

      // Give both employees a 10% raise
      employee1.giveRaise();
      employee2.giveRaise();

      // Display the employee information again
      System.out.printf("%nAfter 10%% raise:%n");
      System.out.printf("Employee 1: %s %s, Salary: $%.2f%n",
         employee1.getFirstName(), employee1.getLastName(), employee1.getSalary());
      System.out.printf("Employee 2: %s %s, Salary: $%.2f%n",
         employee2.getFirstName(), employee2.getLastName(), employee2.getSalary());
   }
}
