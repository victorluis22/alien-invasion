import pygame
import pygame.mixer
from pygame.sprite import Sprite

class Bala(Sprite):
    """Representa os projéteis do jogo."""
    
    def __init__(self, tela, config, nave):
        """"
        Cria um objeto para o projétil na posição atual da
        espaçonave
        """
        super().__init__()
        self.tela = tela
        
        # Cria um retângulo para o projétil em (0, 0) e, em seguida,
        # define a posição correta
        self.rect = pygame.Rect(0, 0, config.bala_largura, config.bala_altura)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top
        
        # Armazena a posição do projétil como um valor decimal
        self.y = float(self.rect.y)
        
        self.cor = config.bala_cor
        self.velocidade = config.bala_velocidade
        self.som = pygame.mixer.music.load('sons/nave_bala.mp3')
        
    def update(self):
        """Move o projétil para cima na tela."""
        # Atualiza a posição decimal do projétil
        self.y -= self.velocidade
        
        # Atualiza a posição de rect
        self.rect.y = self.y

    def play_som(self):
        """Emite o som de bala laser"""
        pygame.mixer.music.play()
        
    def drawme(self):
        pygame.draw.rect(self.tela, self.cor, self.rect)
        

