# Take input from the user
numbers = []
for i in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

# Sort numbers into two groups
greater_than_100 = []
less_than_100 = []

for number in numbers:
    if number > 100:
        greater_than_100.append(number)
    else:
        less_than_100.append(number)

# Print the two groups
print("Numbers greater than 100:", greater_than_100)
print("Numbers less than 100:", less_than_100)