turno = input("Qual o turno que você estuda? Digite M para matutino, V para Vespertino ou N para Noturno. ")
if turno == "M" or turno == "m":
    print("Bom dia!")
elif turno == "V" or turno == "v":
    print("Boa Tarde!")
elif turno == "N" or turno == "n":
    print("Boa Noite!")
else:
    print ("Valor Inválido!")
