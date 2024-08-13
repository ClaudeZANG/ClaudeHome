package final_project;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the length of each quadrant: ");
        int length = scanner.nextInt();

        System.out.print("Enter the number of vehicles: ");
        int numVehicles = scanner.nextInt();

        Field field = new Field(length, numVehicles);
        Simulator simulator = new Simulator(field);

        simulator.run(10);  // 模拟运行10个回合
    }
}
