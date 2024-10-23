# Q1
def course_information():
    rooms = {
        'CS101': '3004',
        'CS102': '4501',
        'CS103': '6755',
        'NT110': '1244',
        'CM241': '1411'
    }

    instructors = {
        'CS101': 'Haynes',
        'CS102': 'Alvarado',
        'CS103': 'Rich',
        'NT110': 'Burke',
        'CM241': 'Lee'
    }

    times = {
        'CS101': '8:00 a.m.',
        'CS102': '9:00 a.m.',
        'CS103': '10:00 a.m.',
        'NT110': '11:00 a.m.',
        'CM241': '1:00 p.m.'
    }

    course_number = input("Enter a course number: ")
    if course_number in rooms:
        print(f"Course: {course_number}")
        print(f"Room: {rooms[course_number]}")
        print(f"Instructor: {instructors[course_number]}")
        print(f"Meeting time: {times[course_number]}")
    else:
        print("Invalid course number.")


# 调用函数
if __name__ == "__main__":
    course_information()

# Q2
import random


def capital_quiz():
    capitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        # 添加更多州及其首府...
    }

    states = list(capitals.keys())
    random.shuffle(states)

    correct_count = 0
    for state in states:
        answer = input(f"What is the capital of {state}? ").strip()
        if answer.lower() == capitals[state].lower():
            print("Correct!")
            correct_count += 1
        else:
            print(f"Incorrect. The capital is {capitals[state]}.")

    print(f"\nYou got {correct_count} out of {len(states)} correct.")


# 调用函数
if __name__ == "__main__":
    capital_quiz()




# Q3
def encrypt_file(input_file, output_file, codes):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                encrypted_line = ''.join(codes.get(char, char) for char in line)
                outfile.write(encrypted_line)
        print(f"File '{input_file}' has been encrypted to '{output_file}'.")
    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist.")

def decrypt_file(input_file, codes):
    try:
        with open(input_file, 'r') as infile:
            decrypted_line = ''.join({v: k for k, v in codes.items()}.get(char, char) for char in infile.read())
            print("Decrypted content:")
            print(decrypted_line)
    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist.")

codes = {'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '&', 'c': '1'}  # 示例代码

# 调用加密和解密函数
if __name__ == "__main__":
    encrypt_file('input.txt', 'encrypted.txt', codes)
    decrypt_file('encrypted.txt', codes)




# Q4
def unique_words(filename):
    try:
        with open(filename, 'r') as file:
            words = set(word.strip('.,!?;:"()').lower() for line in file for word in line.split())
            print("Unique words:")
            for word in sorted(words):
                print(word)
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")

# 调用函数
if __name__ == "__main__":
    unique_words('text.txt')


# Q5
def word_frequency(filename):
    try:
        with open(filename, 'r') as file:
            word_count = {}
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip('.,!?;:"()').lower()
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        print("Word Frequency:")
        for word, count in sorted(word_count.items()):
            print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")

# 调用函数
if __name__ == "__main__":
    word_frequency('text.txt')



# Q6
def file_analysis(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            words1 = set(word.strip('.,!?;:"()').lower() for line in f1 for word in line.split())
            words2 = set(word.strip('.,!?;:"()').lower() for line in f2 for word in line.split())

        print("Unique words in both files:", words1 | words2)
        print("Common words in both files:", words1 & words2)
        print("Words in first file but not in second:", words1 - words2)
        print("Words in second file but not in first:", words2 - words1)
        print("Words in either file but not both:", words1 ^ words2)
    except FileNotFoundError:
        print("One or both of the files do not exist.")

# 调用函数
if __name__ == "__main__":
    file_analysis('file1.txt', 'file2.txt')


# Q7
def world_series_winners():
    try:
        with open('WorldSeriesWinners.txt', 'r') as file:
            winners = [line.strip() for line in file]

        team_wins = {}
        year_team = {}
        year = 1903

        for winner in winners:
            if winner not in ("1904", "1994"):  # 跳过没有比赛的年份
                team_wins[winner] = team_wins.get(winner, 0) + 1
                year_team[str(year)] = winner
                year += 1
            else:
                year += 1

        year_input = input("Enter a year between 1903 and 2009: ")
        if year_input in year_team:
            team = year_team[year_input]
            print(f"The {team} won the World Series in {year_input}.")
            print(f"They have won the World Series {team_wins[team]} times.")
        else:
            print("No World Series was played that year.")
    except FileNotFoundError:
        print("The file WorldSeriesWinners.txt does not exist.")

# 调用函数
if __name__ == "__main__":
    world_series_winners()

# Q8
import pickle


def name_email_addresses():
    try:
        with open('contacts.pkl', 'rb') as file:
            contacts = pickle.load(file)
    except (FileNotFoundError, EOFError):
        contacts = {}

    while True:
        print("\nMenu:")
        print("1. Look up an email address")
        print("2. Add a new contact")
        print("3. Change an existing contact")
        print("4. Delete a contact")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name: ")
            print(f"{name}'s email address is {contacts.get(name, 'not found')}.")

        elif choice == '2':
            name = input("Enter the name: ")
            email = input("Enter the email: ")
            contacts[name] = email
            print(f"Contact {name} added.")

        elif choice == '3':
            name = input("Enter the name: ")
            if name in contacts:
                email = input("Enter the new email: ")
                contacts[name] = email
                print(f"Contact {name} updated.")
            else:
                print(f"{name} not found.")

        elif choice == '4':
            name = input("Enter the name: ")
            if name in contacts:
                del contacts[name]
                print(f"Contact {name} deleted.")
            else:
                print(f"{name} not found.")

        elif choice == '5':
            with open('contacts.pkl', 'wb') as file:
                pickle.dump(contacts, file)
            print("Contacts saved.")
            break

        else:
            print("Invalid choice. Please try again.")


# 调用函数
if __name__ == "__main__":
    name_email_addresses()



# Q9
import random

def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def blackjack_simulation():
    deck = [value for value in range(1, 11)] * 4 + [10] * 12  # 1-10 and face cards
    deck += [1] * 4  # Adding Aces

    player1_hand = []
    player2_hand = []

    while deck:
        player1_hand.append(draw_card(deck))
        player2_hand.append(draw_card(deck))

        player1_total = sum(player1_hand)
        player2_total = sum(player2_hand)

        if 1 in player1_hand and player1_total + 10 <= 21:
            player1_total += 10
        if 1 in player2_hand and player2_total + 10 <= 21:
            player2_total += 10

        if player1_total > 21:
            print(f"Player 1 busted with {player1_total}. Player 2 wins!")
            break
        elif player2_total > 21:
            print(f"Player 2 busted with {player2_total}. Player 1 wins!")
            break

        if len(deck) == 0:
            if player1_total == player2_total:
                print("It's a tie!")
            elif player1_total > player2_total:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")

# 调用函数
if __name__ == "__main__":
    blackjack_simulation()


# Q10
def word_index(filename):
    word_dict = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line_num, line in enumerate(lines, start=1):
                words = line.split()
                for word in words:
                    word = word.strip('.,!?;:"()').lower()
                    word_dict.setdefault(word, []).append(line_num)

        with open('index.txt', 'w') as index_file:
            for word in sorted(word_dict.keys()):
                index_file.write(f"{word}: {word_dict[word]}\n")

        print("Word index has been written to 'index.txt'.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")


# 调用函数
if __name__ == "__main__":
    word_index('text.txt')


# Q11
import pickle

def name_email_addresses():
    try:
        with open('contacts.pkl', 'rb') as file:
            contacts = pickle.load(file)
    except (FileNotFoundError, EOFError):
        contacts = {}

    while True:
        print("\nMenu:")
        print("1. Look up an email address")
        print("2. Add a new contact")
        print("3. Change an existing contact")
        print("4. Delete a contact")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name: ")
            print(f"{name}'s email address is {contacts.get(name, 'not found')}.")

        elif choice == '2':
            name = input("Enter the name: ")
            email = input("Enter the email: ")
            contacts[name] = email
            print(f"Contact {name} added.")

        elif choice == '3':
            name = input("Enter the name: ")
            if name in contacts:
                email = input("Enter the new email: ")
                contacts[name] = email
                print(f"Contact {name} updated.")
            else:
                print(f"{name} not found.")

        elif choice == '4':
            name = input("Enter the name: ")
            if name in contacts:
                del contacts[name]
                print(f"Contact {name} deleted.")
            else:
                print(f"{name} not found.")

        elif choice == '5':
            with open('contacts.pkl', 'wb') as file:
                pickle.dump(contacts, file)
            print("Contacts saved.")
            break

        else:
            print("Invalid choice. Please try again.")

# 调用函数
if __name__ == "__main__":
    name_email_addresses()



# Q12
import random

def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def blackjack_simulation():
    deck = [value for value in range(2, 11)] * 4 + [10] * 16 + [1] * 4  # 包含2-10和A的牌，10点代表J、Q、K
    player1_hand = []
    player2_hand = []

    while deck:
        player1_hand.append(draw_card(deck))
        player2_hand.append(draw_card(deck))

        player1_total = sum(player1_hand)
        player2_total = sum(player2_hand)

        # 处理A的情况
        if 1 in player1_hand and player1_total + 10 <= 21:
            player1_total += 10
        if 1 in player2_hand and player2_total + 10 <= 21:
            player2_total += 10

        if player1_total > 21 and player2_total > 21:
            print(f"Both players busted with {player1_total} and {player2_total}. No winner!")
            break
        elif player1_total > 21:
            print(f"Player 1 busted with {player1_total}. Player 2 wins!")
            break
        elif player2_total > 21:
            print(f"Player 2 busted with {player2_total}. Player 1 wins!")
            break

        if len(deck) == 0:
            if player1_total == player2_total:
                print("It's a tie!")
            elif player1_total > player2_total:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")

# 调用函数
if __name__ == "__main__":
    blackjack_simulation()


# Q13
def word_index(filename):
    word_dict = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line_num, line in enumerate(lines, start=1):
                words = line.split()
                for word in words:
                    word = word.strip('.,!?;:"()').lower()
                    word_dict.setdefault(word, []).append(line_num)

        with open('index.txt', 'w') as index_file:
            for word in sorted(word_dict.keys()):
                index_file.write(f"{word}: {word_dict[word]}\n")

        print("Word index has been written to 'index.txt'.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")

# 调用函数
if __name__ == "__main__":
    word_index('text.txt')
