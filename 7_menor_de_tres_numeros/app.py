numbers = []

numbers.append(float(input("Digite o primeiro número\n")))
numbers.append(float(input("Digite o segundo número\n")))
numbers.append(float(input("Digite o terceiro número\n")))

# smaller_value = 9999

# for number in numbers:
#     if (number < smaller_value):
#         smaller_value = number

print('O menor valor dos 3 números é: ', min(numbers))