letter = input("Digite F para Feminino ou M para Masculino\n")

if letter.lower() == "f":
    print("F - Feminino")
elif letter.lower() == "m":
    print(f"M - Masculino")
else:
    print(f"Sexo Inválido")