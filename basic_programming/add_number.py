# Python program to add two numbers

def add_number(num1, num2):
    sum = num1 + num2
    return sum

number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number :"))

result = add_number(number1, number2)
print("The sum is:", result)
