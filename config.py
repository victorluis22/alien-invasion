class Configuracoes():
    """Classe que contém as configurações do jogo"""
    
    def __init__(self):
        """Inicializa configurações estáticas do jogo"""
        # Configurações de tela
        self.tela_fundo = (1200, 600)
        self.background_cor = (230, 230, 230)
    
        # Configurações da nave
        self.nave_limite = 3
        
        # Configurações dos projéteis
        self.bala_largura = 500
        self.bala_altura = 15
        self.bala_cor = (60, 60, 60)
        self.bala_limite = 3
        
        # Configurações dos aliens
        self.frota_velocidade_y = 10
        
        # Taxa de aumento da velocidade 
        self.taxa_velocidade = 1.1
        
        # Taxa de aumento na pontuacao
        self.taxa_pontuacao = 1.5
        
        # Inicializa atributos dinâmicos
        self.init_config_dinamica()
        
    def init_config_dinamica(self):
        """Inicializa configurações dinâmicas do jogo"""
        self.nave_velocidade = 1.5
        self.bala_velocidade = 3
        self.alien_velocidade = 1
        self.frota_direcao = 1 # 1 para direita -1 para esquerda
        
        # Pontuação
        self.alien_pontos = 50
        
    def aumenta_velocidade(self):
        """Aumenta os atributos dinâmicos do jogo"""
        self.nave_velocidade *= self.taxa_velocidade
        self.bala_velocidade *= self.taxa_velocidade
        self.alien_velocidade *= self.taxa_velocidade
        self.alien_pontos = int(self.alien_pontos * self.taxa_pontuacao)

    

        
        
        
