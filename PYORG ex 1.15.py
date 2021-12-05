valor_h_trabalhada = float(input("Quanto você ganha por hora? "))
numero_h_trabalhadas = int(input("Quantas horas você trabalhou esse mês? "))
salario_bruto = valor_h_trabalhada * numero_h_trabalhadas
salario_liquido_ir = salario_bruto - salario_bruto * 0.11
pginss = salario_liquido_ir * 0.08
salario_liquido_ireinss = salario_liquido_ir - pginss
pgsindicato = salario_liquido_ireinss * 0.05
salario_liquido = salario_liquido_ireinss - pgsindicato
print ("O seu salário bruto é %5.2f" % salario_bruto)
print ("O valor recolhido ao INSS é %5.2f" % pginss)
print ("O valor recolhido ao Sindicato é %5.2f" % pgsindicato)
print ("O seu salário líquido é %5.2f" % salario_liquido)