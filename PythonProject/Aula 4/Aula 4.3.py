import os
import shutil
print("======Organizador de ficheiros======")
pasta = input("Digita o caminho da pasta que queres organizar:")
categorias = {
    "Imagens": [".jpg", ".jpeg", ".png"],
    "Documentos": [".doc", ".docx", ".odt", ".pdf" , ".txt"],
    "Áudios": [".mp3" , "wav"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv"],
    "Outros": []
}
for categoria in categorias:
    caminho_subpasta = os.path.join(pasta, categoria)
    if not os.path.exists(caminho_subpasta):
        os.makedirs(caminho_subpasta)
for ficheiro in os.listdir(pasta):  # listdir é uma lista dos ficheiros da pasta
    caminho_ficheiro = os.path.join(pasta, ficheiro)
    # C:\Users\Ana\Downloads -> C:\Users\Ana\Downloads\foto.jpg
    if os.path.isfile(caminho_ficheiro):
        nome, extensao = os.path.splitext(ficheiro)
        movido = False
        for categoria, extensoes in categorias.items():
            if extensao.lower() in extensoes:
                shutil.move(caminho_ficheiro, os.path.join(pasta, categoria, ficheiro))
                movido = True
                break
        if not movido:
            shutil.move(caminho_ficheiro, os.path.join(pasta, "Outros", ficheiro))
print("Organização concluída!")

