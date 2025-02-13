car_names = ['Ferrari', 'Lamborghini', 'Porsche', 'Bugatti']

print("Favorite Car Names: ", car_names)

car_to_remove = input("Enter a car name you don't like: ")
car_names.remove(car_to_remove)

car_to_add = input("Enter a car name to replace it: ")
car_names.append(car_to_add)

print("Updated Car Names: ", car_names)