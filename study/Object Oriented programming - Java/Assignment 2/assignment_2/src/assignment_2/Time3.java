package assignment_2;

public class Time3 extends Date3 {
    private int hour;
    private int minute;
    private int second;

    public Time3(int month, int day, int year, int hour, int minute, int second) {
        super(month, day, year);
        if (hour < 0 || hour >= 24) {
            throw new IllegalArgumentException("hour must be 0-23");
        }
        if (minute < 0 || minute >= 60) {
            throw new IllegalArgumentException("minute must be 0-59");
        }
        if (second < 0 || second >= 60) {
            throw new IllegalArgumentException("second must be 0-59");
        }
        this.hour = hour;
        this.minute = minute;
        this.second = second;
    }

    public void tick() {
        if (second < 59) {
            second++;
        } else {
            second = 0;
            incrementMinute();
        }
    }

    public void incrementMinute() {
        if (minute < 59) {
            minute++;
        } else {
            minute = 0;
            incrementHour();
        }
    }

    public void incrementHour() {
        if (hour < 23) {
            hour++;
        } else {
            hour = 0;
            nextDay();
        }
    }

    @Override
    public String toString() {
        return super.toString() + " " + String.format("%02d:%02d:%02d", hour, minute, second);
    }
}
