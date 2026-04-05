# Desenvolva um programa que leia três números e que imprima:
#    2.1. o maior,
#    2.2. o menor,
#    2.3. a soma,
#    2.4. a média.
# Exemplo:
# num1 = 5	num2 = 3	num3 = 10
# **********
# maior = 10
# menor = 3
# soma = 18
# media = 6

num1= float(input("Digite sua primeira nota:"))
num2= float(input("Digite sua segunda nota:"))
num3= float(input("Digite sua terceira nota:"))

n= [num1,num2,num3] #Lista criada para os dados dados pelo usuário 

maior = max(n)  #Valor para cada dado
menor = min(n)
soma = sum(n)
media = soma / 3

print("-------------------------")
print(f"maior = {maior}")
print(f"menor = {menor}")
print(f"soma = {soma}")
print(f"media = {media:.2f}")
print("------------------------")
