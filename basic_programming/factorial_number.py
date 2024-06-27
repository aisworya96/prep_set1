# You have been given a positive integer N. You need to find and print the Factorial of this number.
# The Factorial of a positive integer N refers to the product of all number in the range from 1 to N.


# def factorial(N):
#     result = 1
#     for i in range(1, N + 1):
#         result *= i
#     return result
#
# # Example usage
# N = int(input("Enter a positive integer: "))
# print(f"The factorial of {N} is {factorial(N)}")


# Given two positive integers a and b, return the number of common factors of a and b. An integer x is a common factor of a and b if x divides both a and b.
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)