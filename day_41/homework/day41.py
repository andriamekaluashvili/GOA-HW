"""გადმოგვეცემა რიცხვებით სავსე 
სია, ჩვენ ამ სიიდან უნდა შევკრიბოთ 
ყველა ხუთის ჯერადი რიცხვი და დავბეჭდოთ მათი ჯამი """

number_list = input("enter the list of the numbers:")

numbers = [
     for num in number_list] 

sum = 0

for num in  number_list:
    if num % 5 == 0:
        sum += num

print("5 jeradebia:", sum)
