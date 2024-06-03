# You have been given a positive integer N. You need to find and print the Factorial of this number.
# The Factorial of a positive integer N refers to the product of all number in the range from 1 to N.


def factorial(N):
    result = 1
    for i in range(1, N + 1):
        result *= i
    return result

# Example usage
N = int(input("Enter a positive integer: "))
print(f"The factorial of {N} is {factorial(N)}")
