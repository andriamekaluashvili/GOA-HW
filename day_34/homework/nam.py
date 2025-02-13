# Create a list of group members' names
group_members = ['andria qorchilava', 'saba kublashvili', 'andria shanava',]

# Print the middle 10 students
middle_students = group_members[5:15]
print("Middle 10 students:", middle_students)

# Create a list of alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Search for 'g', 'o', and 'a' in the list of alphabets
search_letters = ['g', 'o', 'a']
found_letters = [letter for letter in alphabets if letter in search_letters]

# Concatenate the found letters and print
goa = ''.join(found_letters)
print("Concatenated letters:", goa)