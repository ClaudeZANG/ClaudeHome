package final_project;

import java.util.ArrayList;
import java.util.List;

public abstract class Vehicle {
    protected int x;
    protected int y;
    protected boolean alive;
    protected List<String> trajectory;

    public Vehicle(int x, int y) {
        this.x = x;
        this.y = y;
        this.alive = true;
        this.trajectory = new ArrayList<>();
        recordPosition();
    }

    public abstract void move() throws Exception;

    protected void recordPosition() {
        trajectory.add(String.format("(%d, %d)", x, y));
    }

    public List<String> getTrajectory() {
        return trajectory;
    }

    @Override
    public String toString() {
        return String.format("Vehicle at (%d, %d) is %s", x, y, alive ? "alive" : "dead");
    }
}
