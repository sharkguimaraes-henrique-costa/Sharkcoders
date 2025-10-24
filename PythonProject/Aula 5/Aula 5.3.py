def vv(vl, l):
    for v in vl:
        if v > l:
            print(v, "km/h acima do limite!")
        elif v < 0:
            print(v, "Impossível!")
        else:
            print(v, "km/h dentro do limite.")
vc = [120,360,900,12000,1000000000000000000000000000000000]
lu = int(input("Insere o limite de velocidade: "))
vv(vc, lu)