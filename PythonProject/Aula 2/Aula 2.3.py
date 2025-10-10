meta=int(input("Quanto dinheiro deseja guardar?"))
cofre=0
while cofre<meta:
    dinheiro = int(input("Quanto dinheiro queres meter no cofre?"))
    if dinheiro>0:
        cofre += dinheiro
        print("Boa! Já tens" , cofre,"€!    Faltam-te",meta-cofre , "€")
    else:
        print("Número não válido.")
if cofre>meta:
    print("Boa! Conseguiste!")