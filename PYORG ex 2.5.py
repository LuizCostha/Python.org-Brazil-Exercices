np1 = float(input("Digite a primeira nota do aluno: "))
np2 = float(input("Digite a segunda nota do aluno: "))
media =  (np1 + np2)/2
if media == 10:
    print ("Aprovado com Distinção.")
if media >= 7 and media != 10:
    print("Aprovado.")
if media < 7 and media != 10:
    print("Reprovado.")
