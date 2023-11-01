M = int(input("Введите число N: "))
Numero = []
for i in range(M):
    number = int(input("Введите цифру: "))
    Numero.append(number)
reversed_numbers = list(reversed(Numero))
print("Перевернутый:")
for number in reversed_numbers:
    print(number)