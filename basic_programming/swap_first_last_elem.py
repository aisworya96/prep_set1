# Python program to interchange first and last elements in a list
# def interchange_first_last(lst):
#     # Check if the list has at least two elements
#     if len(lst) < 2:
#         return lst  # No change needed for lists with less than 2 elements
#
#     # Swap the first and last elements
#     lst[0], lst[-1] = lst[-1], lst[0]
#
#     return lst
# example_list = [1, 2, 3, 4, 5]
# print("Original list:", example_list)
#
# result_list = interchange_first_last(example_list)
# print("List after interchanging first and last elements:", result_list)


# Python Program to Swap Two Elements in a List

def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3

print(swapPositions(List, pos1-1, pos2-1))