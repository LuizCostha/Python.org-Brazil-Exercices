valorhora = float(input("Digite o valor da sua hora trabalhada: "))
qtdehorastrab = int(input("Digite a quantidade de horas trabalhadas: "))
salariobruto = valorhora * qtdehorastrab
if salariobruto <= 900.00:
    salarioliquidoir = salariobruto
    descontoir = "0"
elif 900.00 < salariobruto <= 1500.00:
    salarioliquidodeir = salariobruto - (0.05 * salariobruto)
    descontoir = "5"
elif 1500.00 < salariobruto <= 2500.00:
    salarioliquidodeir = salariobruto - (0.1 * salariobruto)
    descontoir = "10"
elif salariobruto > 2500.00:
    salarioliquidodeir = salariobruto - (0.2 * salariobruto)
    descontoir = "20"
inss = salariobruto * 0.10
fgts = salariobruto * 0.11
totaldedescontos = (salariobruto - salarioliquidodeir) + inss + fgts
salarioliquidofinal = salariobruto - totaldedescontos
print ("Salário Bruto: (%3.2f * %d) : R$%3.2f " % (valorhora, qtdehorastrab, salariobruto))
print ("(-) IR (%s)                 : R$%3.2f " % (descontoir, salariobruto - salarioliquidodeir))
print ("(-) INSS (10)              : R$%3.2f " % inss)
print ("(-) FGTS (11)              : R$%3.2f " % fgts)
print ("Total de descontos          : R$%3.2f " % totaldedescontos)
print ("Salário líquido             : R$%3.2f " % salarioliquidofinal)

