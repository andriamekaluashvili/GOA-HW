# Function to calculate the sum of multiples of five
def sum_of_multiples_of_five(numbers):
    # Initialize sum variable
    sum_multiples_of_five = 0
    
    # Iterate over each number in the list
    for number in numbers:
        # Check if the number is a multiple of five
        if number % 5 == 0:
            # Add the number to the sum
            sum_multiples_of_five += number
    
    # Return the sum of multiples of five
    return sum_multiples_of_five

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

# Test the function
result = sum_of_multiples_of_five(numbers)
print("Sum of multiples of five:", result)