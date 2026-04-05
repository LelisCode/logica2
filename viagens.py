# Desenvolva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
# 0,45 para viagens mais longas.


D = float(input("Qual distância você percorreu em km?"))

if D >= 200:
    c1= D * 0.50
    print(f"A passagem ficou em torno de {c1:.2f}")
else:
    c2= D* 0.45
    print(f"A passagem ficou em torno de {c2:.2f}")

