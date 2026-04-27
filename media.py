# Peça 4 notas (nota1, nota2, nota3, nota4) de  4 alunos (aluno1, aluno2, aluno3, aluno4), calcule a média final (mf) de cada um e exiba na tela a sua situação escolar:
# O range(1, 5) controla a repetição de 4 alunos
for i in range(1, 5):
   
    n = input(f"\nDigite o nome do aluno {i}: ")
    
    print("-" * 50)
    print(f"MÉDIA DO(A) {n.upper()}")
    print("-" * 50)

  
    n1 = float(input("Digite sua primeira nota: "))
    n2 = float(input("Digite sua segunda nota: "))
    n3 = float(input("Digite sua terceira nota: "))
    n4 = float(input("Digite sua quarta nota: "))

  
    mf = (n1 + n2 + n3 + n4) / 4

   
    print(f"\n>>> Aluno: {n}")
    print(f">>> Média Final: {mf:.1f}")

    if mf >= 7:
        print("SITUAÇÃO: APROVADO")
    elif mf >= 5:
        print("SITUAÇÃO: RECUPERAÇÃO")
    else: 
        print("SITUAÇÃO: REPROVADO")
    
    print("-" * 50) 
