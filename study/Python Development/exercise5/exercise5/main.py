# Q1
def display_numbers():
    try:
        with open('numbers.txt', 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("The file numbers.txt does not exist.")

# 调用函数
if __name__ == "__main__":
    display_numbers()


# Q2
def display_file_head():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            for i in range(5):
                line = file.readline()
                if line == '':
                    break
                print(line.strip())
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# 调用函数
if __name__ == "__main__":
    display_file_head()


# Q3
def display_with_line_numbers():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            line_number = 1
            for line in file:
                print(f"{line_number}: {line.strip()}")
                line_number += 1
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# 调用函数
if __name__ == "__main__":
    display_with_line_numbers()


# Q4
def count_names():
    try:
        with open('names.txt', 'r') as file:
            names = file.readlines()
            print(f"The file contains {len(names)} names.")
    except FileNotFoundError:
        print("The file names.txt does not exist.")

# 调用函数
if __name__ == "__main__":
    count_names()


# Q5
def sum_of_numbers():
    try:
        total = 0
        with open('numbers.txt', 'r') as file:
            for line in file:
                total += int(line.strip())
        print(f"The sum of the numbers is: {total}")
    except FileNotFoundError:
        print("The file numbers.txt does not exist.")
    except ValueError:
        print("The file contains non-numeric data.")

# 调用函数
if __name__ == "__main__":
    sum_of_numbers()


# Q6
def average_of_numbers():
    try:
        total = 0
        count = 0
        with open('numbers.txt', 'r') as file:
            for line in file:
                total += int(line.strip())
                count += 1
        if count == 0:
            print("The file is empty.")
        else:
            print(f"The average of the numbers is: {total / count:.2f}")
    except FileNotFoundError:
        print("The file numbers.txt does not exist.")
    except ValueError:
        print("The file contains non-numeric data.")

# 调用函数
if __name__ == "__main__":
    average_of_numbers()


# Q7
import random

def write_random_numbers():
    filename = input("Enter the filename to write the random numbers: ")
    count = int(input("Enter the number of random numbers to generate: "))

    with open(filename, 'w') as file:
        for _ in range(count):
            random_number = random.randint(1, 500)
            file.write(f"{random_number}\n")

    print(f"{count} random numbers have been written to {filename}.")

# 调用函数
if __name__ == "__main__":
    write_random_numbers()


# Q8
def read_random_numbers():
    filename = input("Enter the filename with random numbers: ")
    try:
        total = 0
        count = 0
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                print(number)
                total += number
                count += 1
        print(f"\nTotal of the numbers: {total}")
        print(f"Number of random numbers read: {count}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except ValueError:
        print("The file contains non-numeric data.")

# 调用函数
if __name__ == "__main__":
    read_random_numbers()


# Q9
def write_golf_scores():
    with open('golf_scores.txt', 'w') as file:
        while True:
            name = input("Enter player's name (or 'quit' to stop): ")
            if name.lower() == 'quit':
                break
            score = input(f"Enter {name}'s score: ")
            file.write(f"{name},{score}\n")

    print("Golf scores have been written to golf_scores.txt.")

# 调用函数
if __name__ == "__main__":
    write_golf_scores()



# Q10
def read_golf_scores():
    try:
        with open('golf_scores.txt', 'r') as file:
            print("Golf Scores:")
            for line in file:
                name, score = line.strip().split(',')
                print(f"Player: {name}, Score: {score}")
    except FileNotFoundError:
        print("The file golf_scores.txt does not exist.")

# 调用函数
if __name__ == "__main__":
    read_golf_scores()



# Q11
def analyze_file():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            char_count = sum(len(line) for line in lines)

        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
        print(f"Characters: {char_count}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# 调用函数
if __name__ == "__main__":
    analyze_file()



# Q12
def convert_to_uppercase():
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                outfile.write(line.upper())
        print(f"Content has been converted to uppercase and saved to {output_filename}.")
    except FileNotFoundError:
        print(f"The file {input_filename} does not exist.")

# 调用函数
if __name__ == "__main__":
    convert_to_uppercase()


