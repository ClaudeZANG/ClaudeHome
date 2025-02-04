package final_project;

public class Tractor extends Vehicle {
    private String type;

    public Tractor(int x, int y) {
        super(x, y);
        this.type = "TRACTOR";
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
        return String.format("Tractor at (%d, %d) is %s", x, y, alive ? "alive" : "dead");
    }
}
