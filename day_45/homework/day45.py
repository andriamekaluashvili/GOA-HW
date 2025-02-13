# Task 1: Practice what you know on the material you have covered
print("Hello, World!")

# Task 2: Think of a task and write the task code
def calculate_sum(a, b):
    return a + b

result = calculate_sum(3, 4)
print("Sum:", result)

# Task 3: Do the task of level 44
def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("Average:", average)