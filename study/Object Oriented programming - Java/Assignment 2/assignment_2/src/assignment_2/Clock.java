package assignment_2;

public class Clock {
    public static void main(String[] args) {
        Time3 time = new Time3(12, 31, 2023, 23, 59, 58);

        for (int i = 0; i < 5; i++) {
            System.out.println(time);
            time.tick();
        }

        for (int i = 0; i < 60 * 24; i++) {
            time.incrementMinute();
        }

        System.out.println("After 24 hours:");
        System.out.println(time);
    }
}
