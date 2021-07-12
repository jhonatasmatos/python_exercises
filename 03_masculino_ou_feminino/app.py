letter = input("Digite F para Feminino ou M para Masculino\n")

if letter.lower() == "f":
    print("F - Feminino")
elif letter.lower() == "m":
    print("M - Masculino")
else:
    print("Sexo Inválido")