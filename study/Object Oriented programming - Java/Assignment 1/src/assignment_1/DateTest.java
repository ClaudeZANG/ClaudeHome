package assignment_1;

public class DateTest {
    public static void main(String[] args) {
        // Create a Date object
        Date date = new Date(7, 4, 2024);

        // Display the date
        System.out.print("The date is: ");
        date.displayDate();

        // Modify the date
        date.setMonth(12);
        date.setDay(25);
        date.setYear(2024);

        // Display the new date
        System.out.print("The new date is: ");
        date.displayDate();
    }
}
