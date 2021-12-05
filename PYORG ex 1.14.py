pesopeixe = float(input("Digite a quantidade de peixe pescada hoje: "))
if pesopeixe <= 50:
    print ("A quantidade de produto pescada hoje está dentro dos limites diários legais. Logo, não há excesso nem multa a pagar. Parabéns. ")
else:
    excesso = pesopeixe - 50
    multa = excesso * 4
    print ("A quantidade de produto pescada hoje está %4.2f quilogramas além dos limites diários legais. Logo, você terá de pagar %6.2f de multa." % (excesso, multa))