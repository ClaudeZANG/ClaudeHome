package filematching;

import java.io.*;
import java.util.*;

public class AlignText {
    public static void main(String[] args) {
        if (args.length < 3) {
            System.out.println("Usage: java AlignText inputFile outputFile width");
            return;
        }

        String inputFile = args[0];
        String outputFile = args[1];
        int width = 0;
        
        try {
            width = Integer.parseInt(args[2]);
        } catch (NumberFormatException e) {
            System.out.println("Error: Width must be an integer.");
            return;
        }

        List<String> lines = new ArrayList<>();

        // 读取输入文件
        try (BufferedReader reader = new BufferedReader(new FileReader(inputFile))) {
            String line;
            while ((line = reader.readLine()) != null) {
                lines.addAll(Arrays.asList(line.split("\\s+")));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 对齐文本
        List<String> alignedLines = alignText(lines, width);

        // 写入输出文件
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile))) {
            for (String alignedLine : alignedLines) {
                writer.write(alignedLine);
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static List<String> alignText(List<String> words, int width) {
        List<String> result = new ArrayList<>();
        int currentWidth = 0;
        StringBuilder line = new StringBuilder();

        for (String word : words) {
            if (currentWidth + word.length() + 1 > width) {
                result.add(justify(line.toString().trim(), width));
                line = new StringBuilder();
                currentWidth = 0;
            }
            line.append(word).append(" ");
            currentWidth += word.length() + 1;
        }

        if (line.length() > 0) {
            result.add(justify(line.toString().trim(), width));
        }

        return result;
    }

    public static String justify(String line, int width) {
        String[] words = line.split("\\s+");
        if (words.length == 1) {
            return words[0];
        }

        int totalSpaces = width - line.replace(" ", "").length();
        int spacesBetweenWords = totalSpaces / (words.length - 1);
        int extraSpaces = totalSpaces % (words.length - 1);

        StringBuilder justified = new StringBuilder();
        for (int i = 0; i < words.length - 1; i++) {
            justified.append(words[i]);
            for (int j = 0; j < spacesBetweenWords; j++) {
                justified.append(" ");
            }
            if (i < extraSpaces) {
                justified.append(" ");
            }
        }
        justified.append(words[words.length - 1]);

        return justified.toString();
    }
}
