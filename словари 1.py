pets = {}
pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")
pets[pet_name] = {
    "Вид питомца": pet_type,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}
if pet_age == 1:
    print(f"Это {pet_type.lower()} по кличке \"{pet_name}\". Возраст питомца: {pet_age} год. Имя владельца: {owner_name}")
else:
    print(f"Это {pet_type.lower()} по кличке \"{pet_name}\". Возраст питомца: {pet_age} лет. Имя владельца: {owner_name}")