import pygame
from pygame.sprite import Sprite


class Nave(Sprite):
    """Classe que representa a nave principal do jogo"""
    
    def __init__(self, config, tela):
        super().__init__()
        self.tela = tela
        
        # Acesso às configurações
        self.config = config
        
        
        # Carrega a imagem da nave e cria retângulos para a nave
        # e para a tela
        self.image = pygame.image.load('imagens/ship.bmp')
        self.rect = self.image.get_rect()
        self.tela_rect = self.tela.get_rect()
        
        
        # Inicializa nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.tela_rect.centerx
        self.rect.bottom = self.tela_rect.bottom
        
        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)
        
        # Flag de movimento
        self.movendo_direita = False
        self.movendo_esquerda = False   
        

    def atualiza(self):
        """
        Atualiza a posição da nave de acordo com a flag de movimento
        """
        # Atualiza a posição de x usando floats
        if self.movendo_direita and self.rect.right < self.tela_rect.right:
            self.center += self.config.nave_velocidade
            
        if self.movendo_esquerda and self.rect.left > 0:
            self.center -= self.config.nave_velocidade
        
        # Atualiza o retângulo com base nos self.center, que permite float
        self.rect.centerx = self.center
        
        
    def blitme(self):
        """Desenha a nave na posição inicial"""
        self.tela.blit(self.image, self.rect)
        
    def centraliza(self):
        """Centraliza a nave se ela for atingida"""
        self.center = self.tela_rect.centerx
