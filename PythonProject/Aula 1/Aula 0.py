# Jogo da Adivinha em Phyton
import random

# Mensagem Inicial
print("Vamoos jogar ao jogo da Adivinha!")
print ("Estou a pensar num número entre 1 e 10...")

#Número secreto
nums=random.randint(1,10)

# O jogador tenta adivinhar
palpite=int(input("Qual é o teu palpite? "))

if palpite == nums:
    print("Boa acertaste!")
elif palpite > nums:
    print("Muito alto!")
    palpite=int(input("Tenta outra vez!"))
else:
    print("Muito Baixo")
    palpite=int(input("Tenta outra vez!"))

    if palpite == nums:
        print("Boa acertaste!")
    elif palpite > nums:
        print("Muito alto!")
        palpite = int(input("Perdeste!"))
    else:
        print("Muito Baixo")
        palpite = int(input("Perdeste!"))
