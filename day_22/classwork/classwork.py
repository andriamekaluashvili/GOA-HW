# საუკეთესო აკადემიის გამოსავლენი პროგრამა
def ask_best_academy():
    # საუკეთესო აკადემია საქართველოში
    correct_answer = "გოა"  # შეცვალეთ აქ თქვენს მიერ სასურველი აკადემიით

    while True:  # მუდმივად გავიმეორებთ კითხვას
        answer = input("რომელი აკადემია არის საუკეთესო საქართველოში? ")

        # თუ პასუხი სწორი არაა, კიდევ ერთხელ ვეკითხებით
        if answer.lower() == correct_answer.lower():
            print("სწორია! გოა ნამდვილად საუკეთესო აკადემია საქართველოში!")
            break  # გამოდის ციკლიდან
        else:
            print("არასწორია! სცადეთ კიდევ ერთხელ.")

# ამ ფუნქციის გაშვება
ask_best_academy()
