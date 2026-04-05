#  lista vazia que armazenara os números
n = []

#  loop de até 5 números
for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    n.append(numero)

# Exibição dos resultados
print("\n Os números digitados foram:")
for n in n:
    print(n)
