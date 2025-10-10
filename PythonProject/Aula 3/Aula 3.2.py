notas = {"Henrique": 20,
         "Eduardo": 17,
         "Afonso": 12,
         "Lucas": 8}

nome = input("Digite o nome do aluno: o teu nome. ")
if nome in notas:
    nota = notas[nome]
    print(nome , ", a tua nota é..." , nota, "de 20.")
    if nota>= 10:
        print("Parabéns! Passaste!")
    else:
        print("Infelizmente, chumbaste.")
else:
    print("Aluno não encontrado.")