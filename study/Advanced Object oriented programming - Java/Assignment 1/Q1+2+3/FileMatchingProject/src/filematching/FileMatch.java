package filematching;

import java.io.*;
import java.util.*;

public class FileMatch {
    public static void main(String[] args) {
        Map<Integer, Account> masterRecords = new TreeMap<>();
        List<TransactionRecord> transactionRecords = new ArrayList<>();

        try (BufferedReader masterReader = new BufferedReader(new FileReader("oldmast.txt"));
             BufferedReader transactionReader = new BufferedReader(new FileReader("trans.txt"))) {
            String line;

            while ((line = masterReader.readLine()) != null) {
                String[] parts = line.split(" ");
                int accountNumber = Integer.parseInt(parts[0]);
                String name = parts[1] + " " + parts[2];
                double balance = Double.parseDouble(parts[3]);
                masterRecords.put(accountNumber, new Account(accountNumber, name, balance));
            }

            while ((line = transactionReader.readLine()) != null) {
                String[] parts = line.split(" ");
                int accountNumber = Integer.parseInt(parts[0]);
                double amount = Double.parseDouble(parts[1]);
                transactionRecords.add(new TransactionRecord(accountNumber, amount));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        try (BufferedWriter masterWriter = new BufferedWriter(new FileWriter("newmast.txt"));
             BufferedWriter logWriter = new BufferedWriter(new FileWriter("log.txt"))) {
            for (TransactionRecord transaction : transactionRecords) {
                if (masterRecords.containsKey(transaction.getAccountNumber())) {
                    masterRecords.get(transaction.getAccountNumber()).combine(transaction);
                } else {
                    logWriter.write("Unmatched transaction record for account number " + transaction.getAccountNumber());
                    logWriter.newLine();
                }
            }

            for (Account account : masterRecords.values()) {
                masterWriter.write(account.getAccountNumber() + " " + account.getName() + " " + account.getBalance());
                masterWriter.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
