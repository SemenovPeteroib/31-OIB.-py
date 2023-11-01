A = int(input())
numbers = list(map(int, input().split()))
reversed_numbers = numbers[::-1]
for Nomer in reversed_numbers:
    print(Nomer, end=" ")
