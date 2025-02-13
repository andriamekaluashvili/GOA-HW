# რეალური პაროლი
real_password = "mysecretpassword"  # შეცვალეთ თქვენი პაროლით

def ask_for_password():
    while True:  # ვიმეორებთ კითხვას მანამ, სანამ პაროლი სწორად არ შეყვანილი
        user_password = input("შეიყვანეთ პაროლი: ")  # მომხმარებლის პაროლის შეყვანა

        if user_password == real_password:  # თუ პაროლი სწორი არის
            print("წარმატებით შევდივართ ექაუნთზე!")
            break  # გამოდის ციკლიდან
        else:
            print("არასწორია პაროლი! სცადეთ კიდევ ერთხელ.")

# ამ ფუნქციის გაშვება
ask_for_password()
