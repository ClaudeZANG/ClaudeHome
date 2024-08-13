package assignment_2;

public class HourlyEmployee extends Employee {
    private double wage;
    private double hours;

    public HourlyEmployee(String firstName, String lastName, String socialSecurityNumber, double wage, double hours) {
        super(firstName, lastName, socialSecurityNumber);
        this.wage = wage;
        this.hours = hours;
    }

    @Override
    public double earnings() {
        return wage * hours;
    }

    @Override
    public String toString() {
        return String.format("Hourly Employee: %s\nHourly Wage: %.2f\nHours Worked: %.2f",
            super.toString(), wage, hours);
    }
}
