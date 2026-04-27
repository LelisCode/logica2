#Um caixa eletrônico permite 3 tentativas para digitar a senha correta (4321). 
# Caso erre 3 vezes, a conta será bloqueada.


SC = "4321"
T = 3  # Removidas as aspas para ser um número

while T > 0:
    S = input("Digite sua senha: ")
    if S == SC:
        print("acesso liberado")
        break
    else:
        T -= 1
        if T == 0:
            print("Conta bloqueada")
        else:
            print(f"Senha incorreta! Você tem mais {T} tentativa(s).")
