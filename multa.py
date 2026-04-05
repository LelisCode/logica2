# Desenvolva um programa que pergunte a velocidade do carro de um usuário. 
# Se a velocidade ultrapassar 80km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 50,00 por cada km acima de 80 km/h.
# Exemplo: Digite a velocidade em Km/h: 85
# Limite = 80Km/h
# Excedeu 5Km/h
# multa = 5Km/h * R$ 50,00
# Valor da multa: R$ 250,00

v = int(input("Digite a velocidade em Km/h:"))
l = 80 

if v >= l :

 e= v-l
 m= e * 50
 print(f"Você excedeu a velocidade, sua multa será de {m} R$")

else:
 print (f"Você não excedeu a velocidade, está sem multa!")


