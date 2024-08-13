package assignment_2;

public class SalariedEmployee extends Employee {
    private double salary;

    public SalariedEmployee(String firstName, String lastName, String socialSecurityNumber, double salary) {
        super(firstName, lastName, socialSecurityNumber);
        this.salary = salary;
    }

    @Override
    public double earnings() {
        return salary;
    }

    @Override
    public String toString() {
        return String.format("Salaried Employee: %s\nWeekly Salary: %.2f",
            super.toString(), salary);
    }
}
