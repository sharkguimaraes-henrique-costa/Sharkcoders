import os
pp = input("Escreve o caminho da pasta onde queres criar algum ficheiro.")
np = input("Escreve o nome da nova pasta.")
cn = os.path.join(pp, np)
if not os.path.exists(cn):
    os.mkdir(cn)
    print("Pasta criada com sucesso!")
else:
    print("Essa pasta já existe!")

