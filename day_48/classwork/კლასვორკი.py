# Task 0
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(elements)

# Task 1
empty_list = []
for _ in range(1000):
    empty_list.append("❤️")
print(empty_list)

# Task 2
chosen_word = input("Enter a word: ")
while len(chosen_word) > 6:
    print("The word should not exceed 6 characters.")
    chosen_word = input("Enter a word: ")

# Task 3
empty_list2 = []
for _ in range(2):
    new_list = []
    for i in range(5):
        new_list.append(i)
    empty_list2.append(new_list)
print(empty_list2)

# Task 4
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name) gone