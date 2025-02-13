for i in range(21):  # range(21) იძლევა რიცხვებს 0-დან 20-მდე
    print(i)
for i in range(1, 11):
    print(i)
# პარიზული რიცხვები
print("პარიზული რიცხვები:")
for i in range(0, 101, 2):  # 0-დან იწყება, ნაბიჯი 2-ს (პარიზული რიცხვები)
    print(i)

# უხარისხო რიცხვები
print("\nუხარისხო რიცხვები:")
for i in range(1, 101, 2):  # 1-დან იწყება, ნაბიჯი 2-ს (უხ_qualityო რიცხვები)
    print(i)
sum_numbers = 0
for i in range(1, 11):
    sum_numbers += i
print("რიცხვების ჯამი 1-დან 10-მდე:", sum_numbers)
# მომხმარებლისგან რიცხვის მიღება
n = int(input("მიუთითეთ რიცხვი: "))

# ჯამის გამოთვლა
sum_up_to_n = 0
for i in range(1, n + 1):
    sum_up_to_n += i

print(f"ჯამი 1-დან {n}-მდე:", sum_up_to_n)
for i in range(1, 16):
    print(f"{i}-ის კვადრატი არის {i ** 2}")
