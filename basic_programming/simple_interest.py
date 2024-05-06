# Python program to find simple interest

def find_simple_interest(principle,time,rate):

    interest = (principle * time * rate) / 100
    return interest

principle_amount = float(input("Enter the Principle Amount: "))
time_period = float(input("Enter the time period: "))
interest_rate = float(input("Enter the interest rate:"))
simple_interest = find_simple_interest(principle_amount, time_period, interest_rate)
print("Simple Interest: ", simple_interest )


