# # Q1
# def recursive_print(n):
#     if n > 0:
#         recursive_print(n - 1)
#         print(n)
#
# def main():
#     n = int(input("Enter a positive integer: "))
#     recursive_print(n)
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
# # Q2
# def recursive_multiply(x, y):
#     if y == 1:
#         return x
#     else:
#         return x + recursive_multiply(x, y - 1)
#
# def main():
#     x = int(input("Enter the first positive integer: "))
#     y = int(input("Enter the second positive integer: "))
#     result = recursive_multiply(x, y)
#     print(f"{x} * {y} = {result}")
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
# # Q3
# def recursive_lines(n):
#     if n > 0:
#         recursive_lines(n - 1)
#         print('*' * n)
#
# def main():
#     n = int(input("Enter the number of lines: "))
#     recursive_lines(n)
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
#
# # Q4
# def recursive_largest(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         max_rest = recursive_largest(lst[1:])
#         return max(lst[0], max_rest)
#
# def main():
#     lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
#     print(f"Largest number in the list: {recursive_largest(lst)}")
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
#
# # Q5
# def recursive_sum(lst):
#     if len(lst) == 0:
#         return 0
#     else:
#         return lst[0] + recursive_sum(lst[1:])
#
# def main():
#     lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
#     print(f"Sum of the list: {recursive_sum(lst)}")
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
#
# # Q6
# def recursive_sum_numbers(n):
#     if n == 1:
#         return 1
#     else:
#         return n + recursive_sum_numbers(n - 1)
#
# def main():
#     n = int(input("Enter a positive integer: "))
#     print(f"Sum of numbers from 1 to {n}: {recursive_sum_numbers(n)}")
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
#
#
# # Q7
# def recursive_power(x, y):
#     if y == 0:
#         return 1
#     else:
#         return x * recursive_power(x, y - 1)
#
# def main():
#     x = int(input("Enter the base number: "))
#     y = int(input("Enter the exponent (nonnegative integer): "))
#     print(f"{x} raised to the power {y} is {recursive_power(x, y)}")
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
#
# # Q8
# def ackermann(m, n):
#     if m == 0:
#         return n + 1
#     elif n == 0:
#         return ackermann(m - 1, 1)
#     else:
#         return ackermann(m - 1, ackermann(m, n - 1))
#
# def main():
#     m = int(input("Enter a nonnegative integer for m: "))
#     n = int(input("Enter a nonnegative integer for n: "))
#     print(f"Ackermann({m}, {n}) = {ackermann(m, n)}")
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
#
