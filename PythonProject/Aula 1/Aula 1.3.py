print("Vamos ver a tua geração!")
nm=input("Qual é o teu nome?")
an=int(input("Qual foi o ano em que nasceste?"))

#Gerações
if an>=1883 and an<=1900:
    print(nm , "és da geração perdida!")
elif an>1900 and an<=1927:
    print(nm, "és da geração grandiosa!")
elif