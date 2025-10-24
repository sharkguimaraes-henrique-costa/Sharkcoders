class Carro:
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca
        self.velocidade = 0
    def acelerar(self, valor):
        self.velocidade += valor
        print(f"O carro agora vai a {self.velocidade} km/h")
    def travar(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"O carro agora vai a {self.velocidade} km/h")
meu_carro = Carro("vermelho", "Fiat")
carro_amigo = Carro("azul", "Toyota")
meu_carro.acelerar(30)
carro_amigo.acelerar(50)
meu_carro.travar(10)
