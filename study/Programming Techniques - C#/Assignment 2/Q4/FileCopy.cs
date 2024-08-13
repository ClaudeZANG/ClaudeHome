using System;
using System.IO;

namespace FileCopy
{
    class Program
    {
        static void Main(string[] args)
        {
            string sourceFilePath = "source.txt";
            string destinationFilePath = "destination.txt";

            // 创建并写入source.txt文件
            using (StreamWriter writer = new StreamWriter(sourceFilePath))
            {
                writer.WriteLine("This is the content of the source file.");
            }

            // 复制文件内容到destination.txt
            File.Copy(sourceFilePath, destinationFilePath, true);

            Console.WriteLine("File copied successfully.");
        }
    }
}
