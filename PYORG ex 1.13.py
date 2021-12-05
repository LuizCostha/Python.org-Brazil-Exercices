h = float(input("Digite a altura da pessoa: "))
sexo = input("Essa pessoa é mulher ou homem? Digite h para homem e m para mulher: ")
if sexo == "h":
    pideal = (72.7*h) - 58
    print ("O peso ideal é %4.2f" % pideal)
elif sexo == "m":
    pideal = (62.1*h) - 44.7
    print("O peso ideal é %4.2f" % pideal)
else:
    print ("Para saber o peso ideal da pessoa, você precisa especificar se se trata de homem, digitando m, ou mulher, digitando m.")
