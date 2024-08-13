package final_project;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Field {
    private int length;
    private List<Vehicle> vehicles;
    private List<Vehicle> deadVehicles;

    public Field(int length, int numVehicles) {
        this.length = length;
        this.vehicles = new ArrayList<>();
        this.deadVehicles = new ArrayList<>();

        Random rand = new Random();
        for (int i = 0; i < numVehicles; i++) {
            int x = rand.nextInt(length);
            int y = rand.nextInt(length);
            if (i % 4 == 0) {
                vehicles.add(new Car(x, y));
            } else if (i % 4 == 1) {
                vehicles.add(new Truck(x, y));
            } else if (i % 4 == 2) {
                vehicles.add(new SportsCar(x, y));
            } else {
                vehicles.add(new Tractor(x, y));
            }
        }
    }

    public void kill(Vehicle vehicle) {
        vehicle.alive = false;
        deadVehicles.add(vehicle);
    }

    public List<Vehicle> getVehicles() {
        return vehicles;
    }

    public List<Vehicle> getDeadVehicles() {
        return deadVehicles;
    }

    public void checkBoundaries() {
        for (Vehicle vehicle : vehicles) {
            if (vehicle.alive && (vehicle.x < 0 || vehicle.x >= length || vehicle.y < 0 || vehicle.y >= length)) {
                kill(vehicle);
            }
        }
    }
}
