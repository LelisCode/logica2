
# Desenvolva um programa que receba uma string e exiba a mesma na tela. Se o valor digitado for em branco exibir 'Dado inválido'
s = input("Digite uma string: ")

# Valor do vazio
if s == "":
    print("Dado inválido")
else:
    # Exibir o resultado
    print(f"{s}")