print("Введите числа первого списка, каждое число через пробел!:")
list1 = set(map(int, input().split()))
print("Введите числа первого списка, каждое число через пробел!:")
list2 = set(map(int, input().split()))
intersection = list1 & list2
print("Количество чисел, содержащихся в обоих списках:", len(intersection))