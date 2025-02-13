# Define the input string
input_string = "goa is the best"

# Split the input string by spaces
words = input_string.split()

# Initialize an empty string to store the connected words
connected_string = ""

# Iterate through each word in the list
for word in words:
    # Concatenate the word to the connected string without spaces
    connected_string += word

# Print the connected string
print(connected_string)