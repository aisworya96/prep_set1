# Reverse a  string
def reverse_string(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left = left + 1
        right = right - 1
    return s


s = ["A","i","s","w","o","r","y","a"]
reverse_string(s)
print(s)

# Reverse a string

# Using slicing
str1 = "Analytics Vidhya"
reversed_str1_slicing = str1[::-1]
print("Using slicing:", reversed_str1_slicing)

# Using reversed() and join()
reversed_str1_reversed = ''.join(reversed(str1))
print("Using reversed() and join():", reversed_str1_reversed)

# Using a loop
str2 = ""
for char in str1:
    str2 = char + str2
print("Using a loop:", str2)

# Using a stack
stack = list(str1)
reversed_str1_stack = ""
while stack:
    reversed_str1_stack += stack.pop()
print("Using a stack:", reversed_str1_stack)
