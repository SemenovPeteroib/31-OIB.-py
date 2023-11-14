numbers = input("Введите последовательность чисел через пробел: ").split()
seen_numbers = set()
for number in numbers:
    if int(number) in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers.add(int(number))
