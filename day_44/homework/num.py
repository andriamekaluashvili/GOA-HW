for num in range(1, 51):
    if num % 5 == 0:
        print(num)
        num = 0

while num <= 20:
    print(num)
    num += 2
    num = 1
sum = 0

while num <= 10:
    sum += num
    num += 1

print("Sum of numbers:", sum)
guess = 0
correct_number = 7

while guess != correct_number:
    guess = int(input("Guess a number between 1 and 10: "))

print("Congratulations! You guessed the correct number.")
password = ""
correct_password = "password123"

while password != correct_password:
    password = input("Enter the password: ")

print("Access granted!")
password = ""
correct_password = "password123"

while password != correct_password:
    password = input("Enter the password: ")

print("Access granted!")
import datetime

current_hour = datetime.datetime.now().hour

if current_hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")
    num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
















