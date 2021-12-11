salarioinicial = float(input("Digite o salário do funcionário: "))
if salarioinicial <= 280.00:
    percentual = 0.2
    salario = salarioinicial + salarioinicial * percentual
elif 280.00 < salarioinicial <= 700.00:
    percentual = 0.15
    salario = salarioinicial + salarioinicial * percentual
elif 700.00 < salarioinicial <= 1500.00:
    percentual = 0.1
    salario = salarioinicial + salarioinicial * percentual
elif salarioinicial > 1500.00:
    percentual = 0.05
    salario = salarioinicial + salarioinicial * percentual
print ("O salário antes do reajuste era %3.2f. O percentual de correção do salário foi de %3.2f. O valor do aumento do salário foi %3.2f. O novo salário após aumento é de %3.2f. " % ((salarioinicial, percentual, (salario - salarioinicial), salario)))
