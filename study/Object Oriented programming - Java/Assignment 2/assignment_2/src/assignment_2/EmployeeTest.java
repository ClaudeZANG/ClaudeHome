package assignment_2;

public class EmployeeTest {
    public static void main(String[] args) {
        Employee[] employees = new Employee[3];

        employees[0] = new HourlyEmployee("John", "Doe", "111-11-1111", 20.0, 40);
        employees[1] = new SalariedEmployee("Jane", "Smith", "222-22-2222", 800.0);
        employees[2] = new PieceWorker("Tom", "Brown", "333-33-3333", 10.0, 500);

        for (Employee employee : employees) {
            System.out.println(employee.toString());
            System.out.printf("Earnings: %.2f%n%n", employee.earnings());
        }
    }
}
