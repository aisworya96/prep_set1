# Write a program to find if the given number is prime or not

# Get input from the user
num = int(input("Enter a number: "))

# Initialize a flag variable
flag = False

# Only check for prime if the number is greater than 1
if num > 1:
    # Check for factors from 2 to num-1
    for i in range(2, num):
        if (num % i) == 0:
            # If a factor is found, set the flag to True and break the loop
            flag = True
            break

# Check the flag to determine if the number is prime
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
