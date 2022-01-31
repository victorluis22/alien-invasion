import pygame.font
from pygame.sprite import Group
from nave import Nave

class Pontuacao():
    """Classe para exibir a pontuação do jogo"""
    
    def __init__(self, tela, config, status):
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.config = config
        self.status = status
        
        # Configurações da fonte para as informações
        self.texto_cor = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepara as imagens do menu de pontuacao
        self.prep_imagens()
        
    def prep_imagens(self):
        """Prepara todas as imagens do painel de pontuação"""
        self.prep_pontuacao()
        self.prep_pontuacao_maxima()
        self.prep_nivel()
        self.prep_naves()

    def prep_pontuacao(self):
        """Tranforma a pontuacao em uma imagem renderizada"""
        pontuacao_arredondada = round(self.status.pontuacao, -1)
        pontuacao_str = f'{pontuacao_arredondada:,}'
        self.pontuacao_image = self.font.render(pontuacao_str, True, 
                                                self.texto_cor, 
                                                self.config.background_cor)
                                                
        # Mostra a pontuacao na parte superior direita da tela
        self.pontuacao_rect = self.pontuacao_image.get_rect()
        self.pontuacao_rect.top = 20
        self.pontuacao_rect.right = self.tela_rect.right - 20
        
    def prep_pontuacao_maxima(self):
        """
        Tranforma a pontuacao maxima em uma imagem renderizada
        """
        pont_max_arredondada = round(self.status.pontuacao_maxima, -1)
        pont_max_str = f'{pont_max_arredondada:,}'
        self.pont_max_image = self.font.render(pont_max_str, True, 
                                               self.texto_cor, 
                                               self.config.background_cor)
                                                
        # Mostra a pontuacao na parte superior central da tela
        self.pont_max_rect = self.pont_max_image.get_rect()
        self.pont_max_rect.top = self.pontuacao_rect.top
        self.pont_max_rect.centerx = self.tela_rect.centerx
        
    def prep_nivel(self):
        """Tranforma o nivel do jogo em uma imagem renderizada"""
        nivel_str = str(self.status.nivel)
        self.nivel_image = self.font.render(nivel_str, True, 
                                            self.texto_cor, 
                                            self.config.background_cor)
                                                
        # Mostra o nivel abaixo da pontuação
        self.nivel_rect = self.nivel_image.get_rect()
        self.nivel_rect.top = self.pontuacao_rect.bottom + 10
        self.nivel_rect.right = self.pontuacao_rect.right
        
    def prep_naves(self):
        """Mostra as naves restantes"""
        self.naves = Group()
        
        for numero_nave in range(self.status.naves_restantes):
            nave = Nave(self.config, self.tela)
            nave.rect.x = 10 + (numero_nave * nave.rect.width)
            nave.rect.y = 10
            self.naves.add(nave)
            
        
    def mostra_pontuacao(self):
        """Desenha a pontuacao na tela"""
        self.tela.blit(self.pontuacao_image, self.pontuacao_rect)
        self.tela.blit(self.nivel_image, self.nivel_rect)
        self.tela.blit(self.pont_max_image, self.pont_max_rect)
        self.naves.draw(self.tela)
        
