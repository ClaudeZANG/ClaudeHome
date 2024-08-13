package assignment_2;

public class DateTest {
    public static void main(String[] args) {
        Date date = new Date(12, 31, 2023);

        for (int i = 0; i < 40; i++) {
            System.out.println(date);
            date.nextDay();
        }
    }
}
