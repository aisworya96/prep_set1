# Write a program to print the given number is odd or even.
def find_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = 7
result = find_odd_even(number)
print(f"The number {number} is {result}.")



