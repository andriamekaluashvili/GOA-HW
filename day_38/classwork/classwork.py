# პირველი სია, სადაც შევიტანთ 10 რიცხვს
numbers = []
for i in range(10):
    number = int(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))  # მომხმარებლისგან რიცხვის მოთხოვნა
    numbers.append(number)

# მეორე სია - სადაც შევიტანთ მხოლოდ ლუწ რიცხვებს
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# მესამე სია - სადაც შევიტანთ მხოლოდ კენტ რიცხვებს
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

# შედეგების დაბეჭდვა
print("პირველი სია (ყველა რიცხვი):", numbers)
print("მეორე სია (ლუწი რიცხვები):", even_numbers)
print("მესამე სია (კენტ რიცხვები):", odd_numbers)
