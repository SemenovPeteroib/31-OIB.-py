N = int(input("Введите количество чисел: "))
numbers = list(map(int, input("Введите числа через пробел: ").split()))
unique_numbers = set(numbers)
print("Количество различных чисел:", len(unique_numbers))