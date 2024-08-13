package filematching;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class CreateData {
    public static void main(String[] args) {
        String[] masterData = {
            "100 Alan Jones 348.17",
            "300 Mary Smith 27.19",
            "500 Sam Sharp 0.00",
            "700 Suzy Green -14.22"
        };

        String[] transactionData = {
            "100 27.14",
            "300 62.11",
            "400 100.56",
            "900 82.17"
        };

        try (BufferedWriter masterWriter = new BufferedWriter(new FileWriter("oldmast.txt"));
             BufferedWriter transactionWriter = new BufferedWriter(new FileWriter("trans.txt"))) {
            for (String record : masterData) {
                masterWriter.write(record);
                masterWriter.newLine();
            }
            for (String record : transactionData) {
                transactionWriter.write(record);
                transactionWriter.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
