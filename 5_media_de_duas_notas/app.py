grade1 = float(input("Digite a primeira nota\n"))
grade2 = float(input("Digite a segunda nota\n"))

average = (grade1 + grade2) / 2

if average == 10:
    print("Aprovado com Distinção")
elif average < 7:
    print("Reprovado")
elif average >= 7:
    print("Aprovado")