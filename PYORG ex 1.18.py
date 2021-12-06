size = float(input("Qual o tamanho em MB do arquivo para download? "))
velocity = float(input("Qual a velocidade em Mbps da sua internet? "))
print ("O tempo aproximado de download do arquivo é de %4.2f minuto(s)." % ((size/velocity) / 60))
