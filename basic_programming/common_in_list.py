# Find the common element from the given two list

def find_common_element(list1, list2):
    c = []
    count = 0
    for i in list1:
        for j in list2:
            if i == j:
                c.append(i)
                count = count + 1
    return c

list1 = [20, 1, 4, 38, 2]
list2 = [1, 2, 60, 4]

count = find_common_element(list1, list2)
print("The common element in both the list: ", count)



