produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))
if produto1 < produto2 and produto1 < produto3:
    print("Você deve comprar o produto de R$%3.2f. " % produto1)
elif produto2 < produto3 and produto2 < produto1:
    print ("Você deve comprar o produto de R$%3.2f." % produto2)
elif produto3 < produto1 and produto3 < produto2:
    print("Você deve comprar o produto de R$%3.2f." % produto3)
