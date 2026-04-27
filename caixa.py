#  O sistema de um caixa eletrônico de uma loja recebe produtos até digitar 0 para finalizar a compra. 
# Durante a compra: somar os valores do produtos
# # Após ser finalizada: Exibir na tela o valor total da  = input("Digite seu nome: ")

n = input("Digite seu nome: ")
print ("-" * 50)

print (f"\nSEJA BEM VINDO A LOJA SENHOR(A) {n.upper()}")

print ("-" * 50)

print ("Escolha seus produtos")



produtos = {
 "Morango": 50.00,
  "Banana": 30.00,
  "Uva": 80.00,
  "Pessêgo": 90.00,
  "Laranja": 20.00

}

carrinho = []
for nome, preco in produtos.items():
    print(f"Produto: {nome:.<15} Valor: R${preco:>6.2f}")

t = 0


while True:
    choise = input("Digite o nome do produto ou (0) para finalizar: ").capitalize() 
    if choise == '0':
        break
    if choise in produtos:
        v = produtos[choise]
      
        t += v
        carrinho.append(choise) 
        
        print (f"\n {carrinho}")
        print (f"\nEste produto sozinho custou {v} R$ ")
        print (f"\nNo total o valor da compra foi {t} R$")