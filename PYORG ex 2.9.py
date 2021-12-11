numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
if numero1 > numero2 > numero3:
    print("A ordem descrescente dos números é: %3.2f, %3.2f e %3.2f. " % (numero1, numero2, numero3))
elif numero1 > numero3 > numero2:
    print("A ordem descrescente dos números é: %3.2f, %3.2f e %3.2f. " % (numero1, numero3, numero2))
elif numero2 > numero3 > numero1:
    print("A ordem descrescente dos números é: %3.2f, %3.2f e %3.2f. " % (numero2, numero3, numero1))
elif numero2 > numero1 > numero3:
    print("A ordem descrescente dos números é: %3.2f, %3.2f e %3.2f. " % (numero2, numero1, numero3))
elif numero3 > numero2 > numero1:
    print("A ordem descrescente dos números é: %3.2f, %3.2f e %3.2f. " % (numero3, numero2, numero1))
elif numero3 > numero1 > numero2:
    print("A ordem descrescente dos números é: %3.2f, %3.2f e %3.2f. " % (numero3, numero1, numero2))


