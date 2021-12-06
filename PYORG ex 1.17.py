area = float(input("Qual a área em metros quadrados a ser pintada? "))
num_litros = area / 6
num_latas = num_litros / 18
num_galoes = num_litros / 3.6
# preco = num_latas * 80
opcao = int(input(
    "Se você pretende comprar somente latas de 18 litros, digite 1. Se você pretende comprar somente galoes de 3.6 litros, digite 2. Se você pretende comprar latas de 18 litros e galoes de 3.6 litros a fim de evitar desperdício, digite 3. "))
if opcao == 1:
    print("Serão necessárias %5.2f latas de 18 litros que custarão %5.2f reais." % (num_latas, num_latas * 80))
elif opcao == 2:
    print("Serão necessários %5.2f galões de 3.6 litros que custarão %5.2f reais." % (num_galoes, num_galoes * 25))
elif opcao == 3:
    num_latasmix = (1.1 * num_litros) // 18
    num_galoesmix = (((1.1 * num_litros % 18) * 18) / 3.6)
    print("Serão necessários %5.2f latas de 18 litros e %4.2f galões de 3.6 litros que custarão %4.2f reais." % (
    num_latasmix, num_galoesmix, (num_latasmix * 80) + (num_galoesmix * 25)))
