def read_lottery_numbers(file_name):
    number_counts = {}

    try:
        with open(file_name, 'r') as file:
            for line in file:
                numbers = line.split()

                for number in numbers:
                    number = int(number)

                    if number in number_counts:
                        number_counts[number] += 1
                    else:
                        number_counts[number] = 1
        return number_counts

    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
        return None


def display_top_and_bottom_numbers(number_counts):
    if number_counts is None:
        return

    sorted_numbers = sorted(number_counts.items(), key=lambda item: item[1], reverse=True)

    print("Top 10 most common numbers:")
    for number, count in sorted_numbers[:10]:
        print(f"Number {number}: {count} times")

    print("\nTop 10 least common numbers:")
    for number, count in sorted_numbers[-10:]:
        print(f"Number {number}: {count} times")


def main():
    file_name = 'pbnumbers.txt'
    number_counts = read_lottery_numbers(file_name)
    display_top_and_bottom_numbers(number_counts)

if __name__ == "__main__":
    main()