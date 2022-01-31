import pygame.font

class Botao():
    """Cria um botão na tela"""
    
    def __init__(self, tela, config, msg):
        self.tela = tela
        self.config = config
        
        # Determina as características do botão
        self.largura, self.altura = 200, 50
        self.botao_cor = (0, 255, 0)
        self.texto_cor = (255, 255, 255)
        self.fonte = pygame.font.SysFont(None, 48)
        
        # Constrói um rect para o botão e para a tela
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.tela_rect = self.tela.get_rect()
        self.rect.center = self.tela_rect.center
        
        # A mensagem do botão deve ser preparada apenas uma vez
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        """
        Transforma msg em uma imagem renderizada 
        e a posiciona no botão
        """
        self.msg_image = self.fonte.render(msg, True, self.texto_cor,
                                          self.botao_cor)
                                          
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_botao(self):
        """Desenha um botão em branco e, em seguida, desenha a mensagem"""
        self.tela.fill(self.botao_cor, self.rect)
        self.tela.blit(self.msg_image, self.msg_image_rect)
        
