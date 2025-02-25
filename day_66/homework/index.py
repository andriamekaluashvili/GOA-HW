1.
def nicknameGenerator(name):

    if len(name) < 3:
        return "Error: Name too short"
    
    vowels = "aeiou"
    
    if len(name) >= 3:
        if name[2] in vowels:
            return name[:4]  # Return first 4 letters if the third letter is a vowel
        else:
            return name[:3]  # Otherwise, return first 3 letters

# Example usage:
print(nicknameGenerator("Samuel"))  # Output: "Sam"
print(nicknameGenerator("Daniel"))  # Output: "Dan"
print(nicknameGenerator("Alison"))  # Output: "Alis"
print(nicknameGenerator("Jo"))      # Output: "Error: Name too short"
2.from collections import Counter

def duplicate_count(s):
    s = s.lower()  # Convert to lowercase to ensure case insensitivity
    counts = Counter(s)  # Count occurrences of each character
    return sum(1 for char, count in counts.items() if count > 1)  # Count distinct characters with more than one occurrence

# Example usage:
print(duplicate_count("aA11"))  # Output: 2 ('a' and '1')
print(duplicate_count("abcde"))  # Output: 0
print(duplicate_count("aabBcde"))  # Output: 2 ('a' and 'b')
print(duplicate_count("Indivisibilities"))  # Output: 2 ('i' and 's')
3.def sum_two_smallest_numbers(numbers):
    numbers.sort()  # Sort the list in ascending order
    return numbers[0] + numbers[1]  # Sum the first two elements

# Example usage:
print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))  # Output: 7 (2 + 5)
print(sum_two_smallest_numbers([10, 343, 5, 7]))    # Output: 12 (5 + 7)
4.def atm_withdrawal(amount):
    if amount % 10 != 0:
        return "Error: Amount must be a multiple of 10"
    
    bills = [100, 50, 20]  # Available bill denominations
    result = []  # List to store the count of each bill

    for bill in bills:
        count, amount = divmod(amount, bill)  # Get number of bills and remaining amount
        result.append(count)

    return tuple(result)  # Return as a tuple (100s, 50s, 20s)

# Example usage:
print(atm_withdrawal(250))   # Output: (2, 1, 0)  -> 2x100 + 1x50
print(atm_withdrawal(370))   # Output: (3, 1, 1)  -> 3x100 + 1x50 + 1x20
print(atm_withdrawal(40))    # Output: (0, 0, 2)  -> 2x20
print(atm_withdrawal(75))    # Output: "Error: Amount must be a multiple of 10"
5.
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))  # Sum the digits of n
    return n

# Example usage:
print(digital_root(16))    # Output: 7 (1 + 6)
print(digital_root(942))   # Output: 6 (9 + 4 + 2 = 15 → 1 + 5 = 6)
print(digital_root(132189)) # Output: 6 (1+3+2+1+8+9 = 24 → 2+4 = 6)
print(digital_root(493193)) # Output: 2 (4+9+3+1+9+3 = 29 → 2+9 = 11 → 1+1 = 2)
def digital_root(n):
    return n if n == 0 else 1 + (n - 1) % 9
6.
def nicknameGenerator(name):
    if len(name) < 3:
        return "Error: Name too short"

    vowels = "aeiou"
    
    # Check if the third letter is a vowel
    if name[2] in vowels:
        return name[:4]  # Return first 4 letters if third letter is a vowel
    else:
        return name[:3]  # Otherwise, return first 3 letters

# Example usage:
print(nicknameGenerator("Samuel"))  # Output: "Sam"
print(nicknameGenerator("Daniel"))  # Output: "Dan"
print(nicknameGenerator("Alison"))  # Output: "Alis"
print(nicknameGenerator("Jo"))      # Output: "Error: Name too short"
7.
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Example usage:
print(is_leap_year(2000))  # Output: True (divisible by 400)
print(is_leap_year(1900))  # Output: False (divisible by 100 but not 400)
print(is_leap_year(2024))  # Output: True (divisible by 4 but not 100)
print(is_leap_year(2023))  # Output: False (not divisible by 4)
8.
def twice_as_old(father_age, son_age):
    return abs(father_age - 2 * son_age)

# Example usage:
print(twice_as_old(36, 18))  # Output: 0 (Father is currently twice as old)
print(twice_as_old(45, 20))  # Output: 5 (5 years ago)
print(twice_as_old(30, 10))  # Output: 10 (10 years ago)
print(twice_as_old(40, 15))  # Output: 10 (In 10 years)
9.
def find_missing_numbers(arr):
    return [num for num in range(arr[0], arr[-1] + 1) if num not in arr]

# Example usage:
print(find_missing_numbers([1, 2, 4, 6, 7, 9]))  # Output: [3, 5, 8]
print(find_missing_numbers([10, 11, 13, 14, 16]))  # Output: [12, 15]
print(find_missing_numbers([3, 4, 5, 6]))  # Output: [] (No missing numbers)
10.
def sum_triangular_numbers(n):
    if n < 1:
        return 0  # If n is less than 1, return 0 (invalid case)
    
    return sum((k * (k + 1)) // 2 for k in range(1, n + 1))

# Example usage:
print(sum_triangular_numbers(4))  # Output: 20 (1 + 3 + 6 + 10)
print(sum_triangular_numbers(6))  # Output: 56 (1 + 3 + 6 + 10 + 15 + 21)
print(sum_triangular_numbers(0))  # Output: 0 (n < 1 case)
print(sum_triangular_numbers(-5)) # Output: 0 (n < 1 case)
11.
def move_zeros_to_end(arr):
    # Filter out all zeros and store non-zero elements in a list
    non_zeros = [x for x in arr if x != 0]
    
    # Count the number of zeros in the original array
    zeros = arr.count(0)
    
    # Combine non-zero elements with the zeros at the end
    return non_zeros + [0] * zeros

# Example usage:
print(move_zeros_to_end([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
print(move_zeros_to_end([0, 0, 1]))         # Output: [1, 0, 0]
print(move_zeros_to_end([1, 2, 3]))         # Output: [1, 2, 3]
print(move_zeros_to_end([0, 0, 0]))         # Output: [0, 0, 0]
12.
import string

def pig_latin(text):
    words = text.split()  # Split the input text into words
    result = []
    
    for word in words:
        # Check if the word contains only alphabets
        if word.isalpha():
            # Move the first letter to the end and add 'ay'
            pig_latin_word = word[1:] + word[0] + "ay"
        else:
            # Keep punctuation marks untouched and just add the word as it is
            pig_latin_word = word
        
        result.append(pig_latin_word)
    
    return " ".join(result)  # Join the list into a single string

# Example usage:
print(pig_latin("Hello world!"))  # Output: "elloHay orldway!"
print(pig_latin("This is a test."))  # Output: "hisTay siay aay esttay."
print(pig_latin("I love programming."))  # Output: "Iay ovelay ogrammingpray."
