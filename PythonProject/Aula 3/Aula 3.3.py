import os

pasta=input("Escreve o nome de uma  pasta:")

if os.path.exists(pasta):
    ficheiros = os.listdir(pasta)
    print("\nAqui estão os ficheiros que encontrei:")
    for f in ficheiros:
        print("-", f)
else:
    print("Essa pasta não existe!")