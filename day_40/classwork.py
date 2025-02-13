# სია, სადაც შევიტანთ 10 რიცხვს
numbers = []

# მომხმარებლისგან 10 რიცხვის მოთხოვნა
for i in range(10):
    number = int(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))
    numbers.append(number)

# ლუწი რიცხვების სია
even_numbers = [num for num in numbers if num % 2 == 0]

# კენტ რიცხვების სია
odd_numbers = [num for num in numbers if num % 2 != 0]

# შედეგის დაბეჭდვა
print("ლუწი რიცხვები:", even_numbers)
print("კენტ რიცხვები:", odd_numbers)
