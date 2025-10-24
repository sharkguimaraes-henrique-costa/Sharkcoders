
import pygame

import random

import sys

import os

# janela

LARGURA = 480

ALTURA = 640

FPS = 60

# cores

BRANCO = (255, 255, 255)

# assets

ASSETS = "assets"


def carregar_img(nome, tamanho=None):
    caminho = os.path.join(ASSETS, nome)

    img = pygame.image.load(caminho).convert_alpha()

    if tamanho:
        img = pygame.transform.smoothscale(img, tamanho)

    return img


class Jogador(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = carregar_img("shark.png", (96, 96))

        self.img_direita = self.image

        self.img_esquerda = pygame.transform.flip(self.img_direita, True, False)

        self.rect = self.image.get_rect()

        self.rect.centerx = LARGURA // 2

        self.rect.bottom = ALTURA - 20

        self.vel = 0

        self.virado_direita = True

    def update(self):

        teclas = pygame.key.get_pressed()

        self.vel = 0

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.vel = -6

            self.image = self.img_esquerda

            self.virado_direita = False

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.vel = 6

            self.image = self.img_direita

            self.virado_direita = True

        self.rect.x += self.vel

        # limitar aos limites da janela

        if self.rect.left < 10:
            self.rect.left = 10

        if self.rect.right > LARGURA - 10:
            self.rect.right = LARGURA - 10


class Peixe(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = carregar_img("fish.png", (40, 28))

        self.rect = self.image.get_rect()

        self.vely = 2.5 + random.uniform(0, 2)

        self.reset_pos()

    def reset_pos(self):
        self.rect.x = random.randint(20, LARGURA - 20 - self.rect.width)

        self.rect.y = random.randint(-300, -40)

    def update(self):
        self.rect.y += self.vely

        if self.rect.top > ALTURA + 8:
            self.reset_pos()


class Mina(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = carregar_img("mine.png", (32, 32))

        self.rect = self.image.get_rect()

        self.vely = 3.2 + random.uniform(0, 2)

        self.reset_pos()

    def reset_pos(self):
        self.rect.x = random.randint(20, LARGURA - 20 - self.rect.width)

        self.rect.y = random.randint(-280, -40)

    def update(self):
        self.rect.y += self.vely

        if self.rect.top > ALTURA + 8:
            self.reset_pos()


def desenhar_texto(surf, texto, tam, x, y, cor=BRANCO, centro=True):
    fonte = pygame.font.SysFont("arial", tam)

    img = fonte.render(texto, True, cor)

    rect = img.get_rect()

    if centro:

        rect.center = (x, y)

    else:

        rect.topleft = (x, y)

    surf.blit(img, rect)


def ecran_game_over(surf, pontuacao, bg):
    surf.blit(bg, (0, 0))

    desenhar_texto(surf, "Game Over", 48, LARGURA // 2, ALTURA // 2 - 40)

    desenhar_texto(surf, f"Pontuação: {pontuacao}", 28, LARGURA // 2, ALTURA // 2 + 10)

    desenhar_texto(surf, "R = reiniciar | ESC = sair", 20,

                   LARGURA // 2, ALTURA // 2 + 60)

    pygame.display.flip()

    esperar = True

    while esperar:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()

                sys.exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()

                    sys.exit()

                if evento.key == pygame.K_r:
                    esperar = False


def main():
    pygame.init()

    pygame.display.set_caption("Shark Dodger")

    ecran = pygame.display.set_mode((LARGURA, ALTURA))

    relogio = pygame.time.Clock()

    # fundo

    background = carregar_img("background.jpeg", (LARGURA, ALTURA))

    todos = pygame.sprite.Group()

    peixes = pygame.sprite.Group()

    minas = pygame.sprite.Group()

    jogador = Jogador()

    todos.add(jogador)

    for _ in range(5):
        p = Peixe()

        todos.add(p)

        peixes.add(p)

    for _ in range(4):
        m = Mina()

        todos.add(m)

        minas.add(m)

    pontuacao = 0

    vidas = 3

    tempo = 0

    dif_timer = 0

    a_correr = True

    while a_correr:

        dt = relogio.tick(FPS) / 1000

        tempo += dt

        dif_timer += dt

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                a_correr = False

        # dificuldade progressiva

        if dif_timer > 10:

            dif_timer = 0

            for p in peixes:
                p.vely *= 1.08

            for m in minas:
                m.vely *= 1.08

        todos.update()

        # colisões

        colhidos = pygame.sprite.spritecollide(jogador, peixes, False)

        for p in colhidos:
            pontuacao += 10

            p.reset_pos()

        batidas = pygame.sprite.spritecollide(jogador, minas, False)

        if batidas:

            vidas -= 1

            for m in batidas:
                m.reset_pos()

        # desenhar

        ecran.blit(background, (0, 0))

        todos.draw(ecran)

        desenhar_texto(ecran, f"Pontos: {pontuacao}", 22, 10, 10, centro=False)

        desenhar_texto(ecran, f"Vidas: {vidas}", 22, LARGURA - 120, 10, centro=False)

        pygame.display.flip()

        if vidas <= 0:

            ecran_game_over(ecran, pontuacao, background)

            # reset

            pontuacao = 0

            vidas = 3

            tempo = 0

            dif_timer = 0

            for p in peixes:
                p.reset_pos()

                p.vely = 2.5 + random.uniform(0, 2)

            for m in minas:
                m.reset_pos()

                m.vely = 3.2 + random.uniform(0, 2)

    pygame.quit()


if __name__ == "__main__":
    main()


