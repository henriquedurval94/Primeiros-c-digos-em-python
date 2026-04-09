import os
os.system("cls") or None

print("=-"*25, "CALCULO PRODUTO", "=-"*25)
print()

#Entrada de dados
n1 = input("Digite o primeiro número: ")
n1 = int(n1)
n2 = input("Digite o segundo número: ")
n2 = int(n2)

#Processamento de dados
mult = n1 * n2

#Saida de dados
print()
print("A multiplicação de", n1, "por", n2, "é", mult)
