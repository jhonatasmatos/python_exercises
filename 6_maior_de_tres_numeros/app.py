numbers = []

numbers.append(float(input("Digite o primeiro número\n")))
numbers.append(float(input("Digite o segundo número\n")))
numbers.append(float(input("Digite o terceiro número\n")))

# highest_value = None

# for number in numbers:
#     if (number > highest_value):
#         highest_value = number

print('O maior valor dos 3 números é: ', max(numbers))