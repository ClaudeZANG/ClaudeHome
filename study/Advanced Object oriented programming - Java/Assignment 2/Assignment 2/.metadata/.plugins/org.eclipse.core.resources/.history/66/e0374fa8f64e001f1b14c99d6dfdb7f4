package filematching;

import java.io.*;
import java.util.*;

public class WordFrequency {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java WordFrequency inputFile outputFile");
            return;
        }

        String inputFile = args[0];
        String outputFile = args[1];

        Map<String, Integer> wordCountMap = new HashMap<>();

        // 读取输入文件并统计单词频率
        try (BufferedReader reader = new BufferedReader(new FileReader(inputFile))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] words = line.split("\\W+");
                for (String word : words) {
                    if (!word.isEmpty()) {
                        word = word.toLowerCase();
                        wordCountMap.put(word, wordCountMap.getOrDefault(word, 0) + 1);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 将单词频率写入输出文件
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile))) {
            for (Map.Entry<String, Integer> entry : wordCountMap.entrySet()) {
                writer.write(entry.getKey() + ": " + entry.getValue());
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
