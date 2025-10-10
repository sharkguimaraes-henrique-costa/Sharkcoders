print("Bem vindo ao criador de perfis!")

#Guardar informações
nome=input("Qual é o teu nome?")
idade=int(input("Quantos anos tens?"))
cidade=input("Qual o nome da cidade em que moras?")
hobby=input("Qual é o teu hobby favorito?")
cor=input("Qual é a tua cor preferida?")

#Resumo de respostas
print("\n---Perfil Criado---" )
print("Nome:" , nome)
print("idade:" , idade)
print("cidade:" , cidade)
print("hobby:" , hobby)
print("cor:" , cor)

#Mensagem final
print("\nMuito Bem," , nome + "!")
print("Agora sabemos que tens" , idade , "anos, que gostas de " , hobby , "e a tua cor favorita é" , cor + "!")