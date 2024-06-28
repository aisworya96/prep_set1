# Python | Multiply all numbers in the list
def find_multiplication(my_list):
    result = 1
    for x in my_list:
        result = result * x
    return result
list = [1, 2, 3, 5]
result_list = find_multiplication(list)
print(result_list)