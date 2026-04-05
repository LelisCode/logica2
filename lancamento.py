# Desenvolva um programa para escrever a contagem regressiva do lançamento de um foguete. 
# O programa deve imprimir 10, 9, 8, …, 1, 0 e 'Ignição!' na tela.

cr = []
print("-" * 59)


# Loop de 10 a 0 
for i in range(10, -1, -1):
    cr.append(i)

# Exibição dos números
for n in cr:
    print(n)

# Mensagem final fora do loop
print("Ignição!")

print("-" * 59)