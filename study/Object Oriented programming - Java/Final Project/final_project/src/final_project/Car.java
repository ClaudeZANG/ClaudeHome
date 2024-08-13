package final_project;

public class Car extends Vehicle {
    private String type;

    public Car(int x, int y) {
        super(x, y);
        this.type = "CAR";
    }

    @Override
    public void move() {
        if (alive) {
            // Car 的移动逻辑
            if (Math.random() < 0.5) {
                x += (Math.random() < 0.5 ? -1 : 1);
            } else {
                y += (Math.random() < 0.5 ? -1 : 1);
            }
            recordPosition(); // 记录当前位置
        }
    }

    @Override
    public String toString() {
        return String.format("Car at (%d, %d) is %s", x, y, alive ? "alive" : "dead");
    }
}
