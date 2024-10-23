# # Q1
# def get_initials():
#     full_name = input("Enter your first, middle, and last name: ")
#     initials = [name[0].upper() for name in full_name.split()]
#     print("Initials:", '. '.join(initials) + '.')
#
# # 调用函数
# if __name__ == "__main__":
#     get_initials()
#
#
# # Q2
# def sum_of_digits():
#     digits = input("Enter a series of single-digit numbers: ")
#     total = sum(int(digit) for digit in digits if digit.isdigit())
#     print(f"The sum of the digits is: {total}")
#
# # 调用函数
# if __name__ == "__main__":
#     sum_of_digits()
#
#
# # Q3
# def date_printer():
#     date_str = input("Enter a date (mm/dd/yyyy): ")
#     month, day, year = date_str.split('/')
#     months = ["January", "February", "March", "April", "May", "June",
#               "July", "August", "September", "October", "November", "December"]
#     month_name = months[int(month) - 1]
#     print(f"{month_name} {int(day)}, {year}")
#
# # 调用函数
# if __name__ == "__main__":
#     date_printer()
#
#
#
# # Q4
# MORSE_CODE_DICT = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#     'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#     'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#     'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
#     '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
#     '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
#     ' ': '/'
# }
#
# def text_to_morse():
#     text = input("Enter a text to convert to Morse code: ").upper()
#     morse_code = ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)
#     print(f"Morse Code: {morse_code}")
#
# # 调用函数
# if __name__ == "__main__":
#     text_to_morse()
#
#
# # Q5
# PHONE_TRANSLATION = {
#     'A': '2', 'B': '2', 'C': '2',
#     'D': '3', 'E': '3', 'F': '3',
#     'G': '4', 'H': '4', 'I': '4',
#     'J': '5', 'K': '5', 'L': '5',
#     'M': '6', 'N': '6', 'O': '6',
#     'P': '7', 'Q': '7', 'R': '7', 'S': '7',
#     'T': '8', 'U': '8', 'V': '8',
#     'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
# }
#
# def translate_phone_number():
#     phone_number = input("Enter a 10-character phone number (XXX-XXX-XXXX): ").upper()
#     translated_number = ''.join(PHONE_TRANSLATION.get(char, char) for char in phone_number)
#     print(f"Translated phone number: {translated_number}")
#
# # 调用函数
# if __name__ == "__main__":
#     translate_phone_number()
#
#
# # Q6
# def average_number_of_words():
#     try:
#         with open('text.txt', 'r') as file:
#             sentences = file.readlines()
#             total_words = sum(len(sentence.split()) for sentence in sentences)
#             average_words = total_words / len(sentences)
#             print(f"Average number of words per sentence: {average_words:.2f}")
#     except FileNotFoundError:
#         print("The file text.txt does not exist.")
#
# # 调用函数
# if __name__ == "__main__":
#     average_number_of_words()
#
#
#
# # Q7
# def character_analysis():
#     try:
#         with open('text.txt', 'r') as file:
#             content = file.read()
#             uppercase_count = sum(1 for char in content if char.isupper())
#             lowercase_count = sum(1 for char in content if char.islower())
#             digit_count = sum(1 for char in content if char.isdigit())
#             whitespace_count = sum(1 for char in content if char.isspace())
#
#         print(f"Uppercase letters: {uppercase_count}")
#         print(f"Lowercase letters: {lowercase_count}")
#         print(f"Digits: {digit_count}")
#         print(f"Whitespace characters: {whitespace_count}")
#     except FileNotFoundError:
#         print("The file text.txt does not exist.")
#
# # 调用函数
# if __name__ == "__main__":
#     character_analysis()
#
#
#
# # Q8
# def capitalize_sentences(text):
#     sentences = text.split('. ')
#     capitalized_sentences = [sentence.capitalize() for sentence in sentences]
#     return '. '.join(capitalized_sentences)
#
# def sentence_capitalizer():
#     text = input("Enter a text: ")
#     result = capitalize_sentences(text)
#     print(f"Capitalized text: {result}")
#
# # 调用函数
# if __name__ == "__main__":
#     sentence_capitalizer()
#
#
# # Q9
# def count_vowels_consonants(text):
#     vowels = "aeiouAEIOU"
#     vowel_count = sum(1 for char in text if char in vowels)
#     consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
#     return vowel_count, consonant_count
#
# def vowel_consonant_counter():
#     text = input("Enter a string: ")
#     vowels, consonants = count_vowels_consonants(text)
#     print(f"Number of vowels: {vowels}")
#     print(f"Number of consonants: {consonants}")
#
# # 调用函数
# if __name__ == "__main__":
#     vowel_consonant_counter()
#
# # Q10
# from collections import Counter
#
#
# def most_frequent_character():
#     text = input("Enter a string: ")
#     if not text:
#         print("No text provided.")
#         return
#
#     counter = Counter(text)
#     most_common = counter.most_common(1)[0]
#     print(f"The most frequent character is '{most_common[0]}' with {most_common[1]} occurrences.")
#
#
# # 调用函数
# if __name__ == "__main__":
#     most_frequent_character()
#
#
# # Q11
# def word_separator(text):
#     result = text[0].upper()
#     for char in text[1:]:
#         if char.isupper():
#             result += ' ' + char.lower()
#         else:
#             result += char
#     return result
#
# def separate_words():
#     text = input("Enter a camel case sentence: ")
#     result = word_separator(text)
#     print(f"Separated sentence: {result}")
#
# # 调用函数
# if __name__ == "__main__":
#     separate_words()
#
#
# # Q12
# def to_pig_latin(word):
#     return word[1:] + word[0] + "ay" if len(word) > 1 else word + "ay"
#
# def pig_latin_converter():
#     text = input("Enter a sentence: ")
#     words = text.split()
#     pig_latin_words = [to_pig_latin(word) for word in words]
#     pig_latin_sentence = ' '.join(pig_latin_words)
#     print(f"Pig Latin: {pig_latin_sentence}")
#
# # 调用函数
# if __name__ == "__main__":
#     pig_latin_converter()
#
#
# # Q13
# from collections import Counter
#
# def powerball_analysis():
#     try:
#         with open('pbnumbers.txt', 'r') as file:
#             numbers = [int(num) for line in file for num in line.split() if num.isdigit()]
#             counter = Counter(numbers)
#             most_common_numbers = counter.most_common(5)
#             print("Most common numbers:")
#             for number, frequency in most_common_numbers:
#                 print(f"Number {number} appeared {frequency} times.")
#     except FileNotFoundError:
#         print("The file pbnumbers.txt does not exist.")
#
# # 调用函数
# if __name__ == "__main__":
#     powerball_analysis()
#
# # Q14
# from collections import Counter
#
#
# def powerball_analysis():
#     try:
#         with open('pbnumbers.txt', 'r') as file:
#             numbers = [int(num) for line in file for num in line.split()[:5]]
#             powerball_numbers = [int(line.split()[-1]) for line in file]
#
#         number_counter = Counter(numbers)
#         powerball_counter = Counter(powerball_numbers)
#
#         most_common = number_counter.most_common(10)
#         least_common = number_counter.most_common()[-10:]
#
#         print("10 Most Common Numbers:")
#         for number, count in most_common:
#             print(f"Number {number}: {count} times")
#
#         print("\n10 Least Common Numbers:")
#         for number, count in least_common:
#             print(f"Number {number}: {count} times")
#
#         print("\nFrequency of Numbers 1-69:")
#         for num in range(1, 70):
#             print(f"{num}: {number_counter.get(num, 0)}")
#
#         print("\nFrequency of PowerBall Numbers 1-26:")
#         for num in range(1, 27):
#             print(f"{num}: {powerball_counter.get(num, 0)}")
#
#     except FileNotFoundError:
#         print("The file pbnumbers.txt does not exist.")
#
#
# # 调用函数
# if __name__ == "__main__":
#     powerball_analysis()
#
# # Q15
# import matplotlib.pyplot as plt
#
#
# def gas_prices_analysis():
#     try:
#         with open('GasPrices.txt', 'r') as file:
#             data = [line.strip().split(':') for line in file]
#             data = [(date, float(price)) for date, price in data]
#
#         # Calculate average price per year
#         year_prices = {}
#         for date, price in data:
#             year = date.split('-')[2]
#             if year not in year_prices:
#                 year_prices[year] = []
#             year_prices[year].append(price)
#
#         print("Average Price per Year:")
#         for year, prices in year_prices.items():
#             average_price = sum(prices) / len(prices)
#             print(f"{year}: ${average_price:.2f}")
#
#         # Calculate average price per month
#         month_prices = {}
#         for date, price in data:
#             month = date[:7]  # Extract MM-YYYY
#             if month not in month_prices:
#                 month_prices[month] = []
#             month_prices[month].append(price)
#
#         print("\nAverage Price per Month:")
#         for month, prices in month_prices.items():
#             average_price = sum(prices) / len(prices)
#             print(f"{month}: ${average_price:.2f}")
#
#         # Calculate highest and lowest prices per year
#         print("\nHighest and Lowest Prices per Year:")
#         for year, prices in year_prices.items():
#             highest_price = max(prices)
#             lowest_price = min(prices)
#             highest_date = next(date for date, price in data if price == highest_price and date.endswith(year))
#             lowest_date = next(date for date, price in data if price == lowest_price and date.endswith(year))
#             print(f"{year} - Highest: {highest_price} on {highest_date}, Lowest: {lowest_price} on {lowest_date}")
#
#         # Generate sorted price lists
#         sorted_prices = sorted(data, key=lambda x: x[1])
#         with open('SortedPricesLowToHigh.txt', 'w') as file:
#             for date, price in sorted_prices:
#                 file.write(f"{date}: ${price:.2f}\n")
#
#         sorted_prices.reverse()
#         with open('SortedPricesHighToLow.txt', 'w') as file:
#             for date, price in sorted_prices:
#                 file.write(f"{date}: ${price:.2f}\n")
#
#         print("\nPrice data sorted and saved to 'SortedPricesLowToHigh.txt' and 'SortedPricesHighToLow.txt'.")
#
#     except FileNotFoundError:
#         print("The file GasPrices.txt does not exist.")
#
#
# # 调用函数
# if __name__ == "__main__":
#     gas_prices_analysis()
