letter = input("Digite uma letra\n")
vogals = {"a", "e", "i", "o", "u"}

if letter in vogals:
    print("A letra é vogal")
else:
    print("A letra é consoante")