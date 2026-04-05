# Desenvolver um programa que calcule e exiba a tabuada de hum a dez de um número qualquer.
#     Exemplo:
#     ******************************
#     Informe o número da tabuada: 5
#     ******************************
#     1 x 5 = 5
#     2 x 5 = 10
#     3 x 5 = 15
#     4 x 5 = 20
#     5 x 5 = 25
#     6 x 5 = 30
#     7 x 5 = 35
#     8 x 5 = 40
#     9 x 5 = 45
#     10 x 5 = 50


r = [] # Lista vazia para armazenar os números que serão multiplicados

print("-" * 59)
n = int(input("Informe o número da tabuada: "))
print("-" * 59)

# Loop de 1 a 10
for i in range(1, 11):
    c = i * n
    r.append(c) # Guarda o resultado na lista
    print(f"{i} x {n} = {c}")