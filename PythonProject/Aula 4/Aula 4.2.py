import shutil
o = input("Escreve o caminho completo da pasta que queres mover:")
r = input("Escreve o caminho completo do sítio para onde a queres mover:")
shutil.move(o, r)
print("Ficheiro movido com sucesso!")