# Desenvolva um programa que exiba somente os números pares de um a cem.


numeros = []

print("-" * 59)


# Loop de 1 a 100
for i in range(1, 101):
  
    numeros.append(i)# Guarda o resultado na lista
for n in numeros:
    if n % 2 == 0:
     print(n)

print("-" * 59)