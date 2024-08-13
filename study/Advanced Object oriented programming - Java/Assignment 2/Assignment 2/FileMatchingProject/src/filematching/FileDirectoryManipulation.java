package filematching;

import java.io.IOException;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.HashMap;
import java.util.Map;

public class FileDirectoryManipulation {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java FileDirectoryManipulation directoryPath");
            return;
        }

        String directoryPath = args[0];
        Path startPath = Paths.get(directoryPath);
        Map<String, Integer> fileTypeCounts = new HashMap<>();

        try {
            Files.walkFileTree(startPath, new SimpleFileVisitor<Path>() {
                @Override
                public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) {
                    String fileName = file.getFileName().toString();
                    int dotIndex = fileName.lastIndexOf('.');
                    if (dotIndex != -1 && dotIndex < fileName.length() - 1) {
                        String extension = fileName.substring(dotIndex + 1).toLowerCase();
                        fileTypeCounts.put(extension, fileTypeCounts.getOrDefault(extension, 0) + 1);
                    }
                    return FileVisitResult.CONTINUE;
                }
            });
        } catch (IOException e) {
            e.printStackTrace();
        }

        fileTypeCounts.entrySet().stream()
            .sorted(Map.Entry.comparingByKey())
            .forEach(entry -> System.out.println(entry.getKey() + ": " + entry.getValue()));
    }
}
