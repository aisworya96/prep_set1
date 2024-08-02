# Write a code snippet to generate the square of every element of a list.

# list =[2,6,8,1,4]
# new_list = []
# for x in list:
#     new_list.append(x * x)
# print(new_list)


def find_square(my_list):
    new_list = []
    for x in my_list:
        new_list.append(x * x)
    return new_list

my_list = [1, 2, 3, 4]
print(find_square(my_list))
