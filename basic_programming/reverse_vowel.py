# Reverse Vowels of a String

def reverse_vowels(s):
    # Define a set of vowels for quick lookup
    vowels = set("aeiouAEIOU")
    # Convert the string to a list to modify it in place
    s_list = list(s)
    # Initialize two pointers
    left, right = 0, len(s_list) - 1

    # Loop until the two pointers meet
    while left < right:
        # Move the left pointer until a vowel is found
        if s_list[left] not in vowels:
            left += 1
            continue
        # Move the right pointer until a vowel is found
        if s_list[right] not in vowels:
            right -= 1
            continue
        # Swap the vowels
        s_list[left], s_list[right] = s_list[right], s_list[left]
        # Move both pointers towards the center
        left += 1
        right -= 1

    # Convert the list back to a string and return it
    return ''.join(s_list)

# Example usage:
s = "hello"
print(reverse_vowels(s))  # Output: "holle"

s = "leetcode"
print(reverse_vowels(s))  # Output: "leotcede"
