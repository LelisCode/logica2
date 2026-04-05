# Na última Black Friday, o gerente de uma loja de perfumes colocou todo o seu estoque em promoção, de acordo com a tabela a seguir:

# Código	Condição de Pagamento	Desconto (%)
# 1 À vista (em espécie)                  10
# 2	Cartão de débito	                   5
# 3	Cartão de crédito	                   3
# 4	PIX			                          7.5

# Construa um programa que solicite ao operador do caixa o preço total da venda, bem como a forma de pagamento.
# Ao fim, o programa deve informar o valor final a ser pago.
o = float(input("Digite o preço da compra:"))
o2 = input("Digite a forma de pagamento:")
      
if o2 == "á vista":    #Identifica a forma de pagamento para te dirigir a um determinado desconto
    c1= o * 0.1
    c2= o - c1
    print(f"O valor a ser pago é {c2} R$")
elif o2 == "Cartão de débito":
    c1= o * 0.05
    c2= o - c1
    print(f"O valor a ser pago é {c2} R$")
elif o2 == "Cartão de crédito":
    c1= o * 0.03
    c2= o - c1
    print(f"O valor a ser pago é {c2} R$")
elif o2 == "PIX":
    c1= o * 0.0075
    c2= o - c1
    print(f"O valor a ser pago é {c2} R$")
else:
    print(f"O valor a ser pago é {o}")

