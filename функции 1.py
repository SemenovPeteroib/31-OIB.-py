def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
def factorial_list(num):
    list_factorials = [factorial(i) for i in range(num, 0, -1)]
    return list_factorials
input_num = 3
result = factorial(input_num)
print(result)
print(factorial_list(result))