# Function to iterate over a string and input characters into a list at certain points

def extract_chars_from_string(input_string):
    # Initialize an empty list to store the results
    result_array = []
    
    # Iterate over the string using enumerate to get both index and character
    for index, char in enumerate(input_string):
        # Condition 1: Append the character if its index is even
        if index % 2 == 0:
            result_array.append(char)
        
        # Condition 2: Append the character if it is a vowel (using 'in' operator)
        # This condition is checked in addition to the first condition in this example.
        if char in "aeiouAEIOU":
            result_array.append(char)

    return result_array

# Example Usage:
my_string = "programming"
# The conditions will extract the following characters:
# 'p' (index 0, even), 'r' (index 1, not even, not vowel), 'o' (index 2, even, vowel),
# 'g' (index 3, not even, not vowel), 'r' (index 4, even), 'a' (index 5, not even, vowel),
# 'm' (index 6, even), 'm' (index 7, not even), 'i' (index 8, even, vowel),
# 'n' (index 9, not even), 'g' (index 10, even)

extracted_chars = extract_chars_from_string(my_string)

print(f"Original string: '{my_string}'")
print(f"Extracted characters (array): {extracted_chars}")
