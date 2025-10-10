#Mini batalha Nintendo

print("Nível final de Super Mario!")
print("Escolhe o teu personagem!")
print("1-Mario")
print("2-Luigi")
print("3-Peach")
print("4-Toad")
print("5-Donkey Kong")
print("6-Yoshi")

escolha=int(input("Qual a tua escolha?"))

#Batalha
if escolha == 1:
    print("O Mario usa o Cappy e derrota o Bowser!")
elif escolha == 2:
    print("O Luigi usa o aspirador para derrotar o King Boo!")
elif escolha == 3:
    print("A Peach voa com o seu guarda-chuva e derrota o Kamek!")
elif escolha ==4:
    print("O Toad atira a sua frigideira contra o Bowser Jr. e derrota-o!")
elif escolha == 5:
    print ("O DK atira um barril em chamas contra o King Bob-omb e ele explode!")
elif escolha==6:
    print("O Yoshi chuta uma casca de Koopa e derrota uma manada enorme de Goombas!")
else:
    print("Inválido. O Bowser cospe fogo contra a tua cara. Tens de recomeçar o nível!")