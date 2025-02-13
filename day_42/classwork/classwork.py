# შექმნათ სია, რომელშიც არის დადებითი და უარყოფითი რიცხვები
numbers = [10, -5, 3, -2, 8, -1, 0, 7, -4]

# შემოქმედებითი სია დადებითი და უარყოფითი რიცხვებისთვის
positive_numbers = []
negative_numbers = []

# გაკოტროთ დადებითი და უარყოფითი რიცხვები
for num in numbers:
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)

# შედეგის დაბეჭდვა
print("დადებითი რიცხვები:", positive_numbers)
print("უარყოფითი რიცხვები:", negative_numbers)
