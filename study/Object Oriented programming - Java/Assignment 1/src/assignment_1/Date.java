package assignment_1;

public class Date {
    // Instance variables
    private int month;
    private int day;
    private int year;

    // Constructor to initialize instance variables
    public Date(int month, int day, int year) {
        this.month = month;
        this.day = day;
        this.year = year;
    }

    // Set and get methods for month
    public void setMonth(int month) {
        this.month = month;
    }

    public int getMonth() {
        return month;
    }

    // Set and get methods for day
    public void setDay(int day) {
        this.day = day;
    }

    public int getDay() {
        return day;
    }

    // Set and get methods for year
    public void setYear(int year) {
        this.year = year;
    }

    public int getYear() {
        return year;
    }

    // Method to display the date
    public void displayDate() {
        System.out.printf("%d/%d/%d%n", month, day, year);
    }
}
