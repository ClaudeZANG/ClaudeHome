package assignment_2;

public class DateAndTimeTest {
    public static void main(String[] args) {
        DateAndTime dateTime = new DateAndTime(12, 31, 2023, 23, 59, 58);

        for (int i = 0; i < 5; i++) {
            System.out.println(dateTime);
            dateTime.incrementHour();
        }
    }
}
