letter = input("Digite seu turno de estudos: M-matutino ou V-Vespertino ou N- Noturno\n")

if letter.lower() == "m":
    print("Bom Dia!")
elif letter.lower() == "v":
    print("Boa Tarde!")
elif letter.lower() == "n":
    print("Boa Noite!")
else:
    print("Valor Inválido!")