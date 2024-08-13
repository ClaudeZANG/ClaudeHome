package final_project;

import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Simulator {
    private Field field;

    public Simulator(Field field) {
        this.field = field;
    }

    public void run(int turns) {
        List<Vehicle> vehicles = field.getVehicles();
        for (int turn = 0; turn < turns; turn++) {
            System.out.println("Turn " + (turn + 1) + ":");
            for (Vehicle vehicle : vehicles) {
                try {
                    vehicle.move();
                    System.out.println(vehicle);
                } catch (Exception e) {
                    System.out.println(vehicle + " (DEAD)");
                }
            }
            field.checkBoundaries();
            System.out.println();
        }
        displayResults();
    }

    private void displayResults() {
        List<Vehicle> vehicles = field.getVehicles();
        List<Vehicle> aliveVehicles = vehicles.stream()
            .filter(vehicle -> vehicle.alive)
            .sorted(Comparator.comparingInt(vehicle -> vehicle.getTrajectory().size()))
            .collect(Collectors.toList());

        System.out.println("Top 3 longest surviving vehicles:");
        for (int i = 0; i < Math.min(3, aliveVehicles.size()); i++) {
            Vehicle vehicle = aliveVehicles.get(i);
            System.out.println(vehicle);
            System.out.println("Trajectory: " + vehicle.getTrajectory());
        }

        List<Vehicle> deadVehicles = field.getDeadVehicles();
        System.out.println("Dead vehicles:");
        for (Vehicle vehicle : deadVehicles) {
            System.out.println(vehicle);
            System.out.println("Trajectory: " + vehicle.getTrajectory());
        }
    }
}
