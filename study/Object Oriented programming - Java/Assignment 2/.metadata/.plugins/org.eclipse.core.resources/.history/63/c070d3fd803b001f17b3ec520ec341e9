package assignment_2;

public class DateAndTime extends Date {
    private Time2 time;

    public DateAndTime(int month, int day, int year, int hour, int minute, int second) {
        super(month, day, year);
        time = new Time2(hour, minute, second);
    }

    public void incrementHour() {
        time.incrementHour();
        if (time.toString().equals("00:00:00")) {
            nextDay();
        }
    }

    @Override
    public String toString() {
        return super.toString() + " " + time.toString();
    }

    public String toUniversalString() {
        return super.toString() + " " + time.toUniversalString();
    }
}
