area = float(input("Qual o tamanho em metros quadrados da área a ser pintada? "))
num_litros = area /  3
num_latas = num_litros / 18
preco = num_latas * 80
print ("A pintura exigirá %4.1f latas." % num_latas)
print ("O preço do orçamento para pintura é R$%5.2f." % preco)