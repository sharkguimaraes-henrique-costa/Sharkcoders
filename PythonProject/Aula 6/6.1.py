import random
from collections import defaultdict

# Conjunto de jogadas e regra "quem vence de quem"
J = ("pedra", "papel", "tesoura")
W = {"pedra": "tesoura", "papel": "pedra", "tesoura": "papel"}  # chave vence o valor


def ler():
    """Lê e valida a jogada do utilizador."""
    while True:
        x = input("pedra/papel/tesoura (ou sair): ").strip().lower()
        if x in J or x in ("sair", "q", "exit"):
            return x
        print("Tenta outra vez… (pedra/papel/tesoura)")


def vence(a, b):
    """Devolve 'jogador', 'computador' ou 'empate' para as jogadas a vs b."""
    if a == b:
        return "empate"
    return "jogador" if W[a] == b else "computador"


print(vence("pedra", "papel"))
print(vence("papel", "pedra"))
print(vence("papel", "papel"))


class IA:
    """

    IA simples com duas estratégias:

    - Frequência global: qual jogada o jogador usa mais no total.

    - Transições (Markov ordem 1): dado o último lance do jogador,

    qual tende a ser o próximo.

    """

    def __init__(self):

        # conta total de cada jogada do jogador ->

        # self.freq = {"pedra": 3, "papel": 2, "tesoura": 1}

        self.freq = defaultdict(int)

        # conta de pares (ultimo -> proximo), ou seja,

        # o que o jogador costuma jogar depois de outra jogada.~

        # self.trans = {"pedra": {"pedra": 1, "papel": 2}, "papel": {"tesoura": 3}, ...}

        self.trans = defaultdict(lambda: defaultdict(int))

        # último lance do jogador (para prever o que virá a seguir)

        self.last = None

    def atualizar(self, jog):

        """Atualiza contagens após ver a jogada real do jogador."""

        self.freq[jog] += 1

        if self.last is not None:  # se houver uma jogada anterior

            self.trans[self.last][jog] += 1

        self.last = jog  # atualiza last

    def prever(self):

        """

        Prevê a próxima jogada do jogador:

        1) Se conhecer o último lance e houver dados de transição, usa Markov.

        2) Caso contrário, usa a jogada mais frequente globalmente.

        3) Sem dados (início), escolhe aleatório.

        """

        # Se eu sei qual foi a última jogada do jogador (self.last)

        # e já tenho informações guardadas sobre o que ele costuma jogar depois dessa jogada

        if self.last is not None and self.trans[self.last]:

            return max(self.trans[self.last], key=self.trans[self.last].get)

        elif self.freq:

            return max(self.freq, key=self.freq.get)

        else:

            return random.choice(J)


def contra(x):
    """Dada a jogada prevista do jogador, devolve a jogada que a vence."""

    for k, v in W.items():

        if v == x:
            return k


def main():
    print("\n=== Pedra-Papel-Tesoura com IA ===\n")

    ia = IA()

    score = {"jogador": 0, "computador": 0, "empate": 0}

    acertos = 0

    tot = 0

    ronda = 1

    while True:

        print(f"\n— Ronda {ronda} —")

        j = ler()

        if j in ("sair", "q", "exit"):
            break

        # IA faz previsão e o PC escolhe o contra-lance que vence essa previsão

        prev = ia.prever()

        pc = contra(prev)

        # Decide vencedor da ronda

        res = vence(j, pc)

        # Atualiza métricas e estado do modelo

        tot += 1

        if prev == j:
            acertos += 1

        score[res] += 1

        ia.atualizar(j)

        # Feedback ao utilizador

        print(f"Tu: {j} | IA previu: {prev} | PC: {pc}")

        print("Resultado:", "Empate" if res == "empate" else ("Ganhaste" if res == "jogador" else "PC venceu"))

        print(f"Placar Tu:{score['jogador']} PC:{score['computador']} Emp:{score['empate']} | "

              f"Acerto IA: {acertos / tot * 100:.1f}%")

        ronda += 1

    if tot:
        print(f"\nTaxa final de acerto da IA: {acertos / tot * 100:.1f}%")

    print("Até já!")


if __name__ == "__main__":
    main()




