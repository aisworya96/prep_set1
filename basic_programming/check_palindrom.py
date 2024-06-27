# Write a program to check if the given number is palindrome or not.

def check_palindrom(num):
    num_str = str(num)
    return num_str == num_str[::-1]
num = int(input("Enter a number: "))

if check_palindrom(num):
    print(num, "is palindrom")
else:
    print(num, "is not palindrom")

