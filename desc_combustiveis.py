# Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#    Álcool:
#       até 20 litros, desconto de 3% por litro
#       acima de 20 litros, desconto de 5% por litro 
#    Gasolina:
#       até 20 litros, desconto de 4% por litro
#       acima de 20 litros, desconto de 6% por litro 

# O programa deverá ler o número de litros vendidos, o tipo de combustível codificado da seguinte forma: 
#    A - Álcool, 
#    G - Gasolina, 
# Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 4,95 o preço do litro do álcool é R$ 2,89

comb = input("Tipo de combustível (A-Álcool / G-Gasolina): ").upper()
lit = float(input("Quantos litros? "))

if comb == "A":   #Ao escolher A poder ter um if ou else que defina as opções dentro dele, o mesmo vale para G
    
    preco_base = 5.00
    if lit <= 20:
        d = 0.03
    else:
        d = 0.05
    valor = lit * (preco_base * (1 - d))
    print(f"Total Álcool: R$ {valor:.2f}")

elif comb == "G":
    preco_base = 3.00
    if lit <= 20:
        d = 0.04
    else:
        d = 0.06
    valor = lit * (preco_base * (1 - d))
    print(f"Total Gasolina: R$ {valor:.2f}")

else:
    print("Tipo de combustível inválido!")
