# Python program to find sum of elements in list
def sum_of_elements(lst):
    total = 0
    for element in lst:
        total += element
    return total

# Example usage
example_list = [1, 2, 3, 4, 5]
total = sum_of_elements(example_list)
print("Sum of elements:", total)