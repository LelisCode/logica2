#Desenvolva um programa que receba um inteiro e exiba o mesmo na tela. Se o valor digitado for em branco exibir 'Dado inválido'
s = int(input("Digite uma string: "))

# Valor do vazio
if s == "":
    print("Dado inválido")
else:
    # Exibir o resultado
    print(f"{s}")