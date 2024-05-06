# find largest and smallest element in an array

def find_largest_and_smallest(arr):
    if not arr:
        return None, None

    largest = arr[0]
    smallest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

        elif num < smallest:
            smallest = num

    return largest, smallest

arr = [67, 37, 89, 34, 1, 2,]

largest, smallest = find_largest_and_smallest(arr)
print("Largest element:", largest)
print("Smallest element:", smallest)

