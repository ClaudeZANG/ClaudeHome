package assignment_2;

public class Date {
    private int month;
    private int day;
    private int year;

    private static final int[] daysPerMonth = 
       { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

    public Date(int month, int day, int year) {
        // Check if month is valid
        if (month <= 0 || month > 12) {
            throw new IllegalArgumentException("Month must be 1-12");
        }

        // Check if day is valid for the month
        if (day <= 0 || 
            (day > daysPerMonth[month] && !(month == 2 && day == 29))) {
            throw new IllegalArgumentException("Day out-of-range for the specified month and year");
        }

        // Check for leap year if month is 2 and day is 29
        if (month == 2 && day == 29 && !(year % 400 == 0 || 
             (year % 4 == 0 && year % 100 != 0))) {
            throw new IllegalArgumentException("Day out-of-range for the specified month and year");
        }

        this.month = month;
        this.day = day;
        this.year = year;

        System.out.printf("Date object constructor for date %02d/%02d/%04d%n", month, day, year);
    }

    public void nextDay() {
        if (day < daysPerMonth[month] || (month == 2 && day == 28 && 
            (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)))) {
            day++;
        } else if (month == 12 && day == 31) {
            day = 1;
            month = 1;
            year++;
        } else {
            day = 1;
            month++;
        }
    }

    @Override
    public String toString() {
        return String.format("%02d/%02d/%04d", month, day, year);
    }
}
