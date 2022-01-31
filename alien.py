import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Classe que representa um alien"""
    
    def __init__(self, tela, config):
        """Inicializa os atributos herdados e outros novos."""
        super().__init__()
        self.tela = tela
        self.config = config
        
        # Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load('imagens/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Inicia cada novo alienígena próximo à parte superior esquerda
        # da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)
        
    def checa_canto(self):
        """
        Verifica se o alienígina está no canto da tela
        Retorna True ou False
        """
        tela_rect = self.tela.get_rect()
        
        if self.rect.right >= tela_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """Move o alienígena para a direita."""
        self.x += self.config.alien_velocidade * self.config.frota_direcao
        self.rect.x = self.x
        
    def blitme(self):
        """Desenha o alien na tela"""
        self.tela.blit(self.image, self.rect)
