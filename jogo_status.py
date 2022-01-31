class JogoStatus():
    """Armazena dados estatísticos do jogo"""
    
    def __init__(self, config):
        self.config = config
        
        # Flag que indica que o jogo está ativo
        self.jogo_ativo = False
        
        # Pontuação máxima
        self.pontuacao_maxima = 0
        
        self.reset_status()
        
    def reset_status(self):
        """
        Inicializa os dados estatísticos que podem mudar durante o
        jogo.
        """
        # Limite de naves por jogo
        self.naves_restantes = self.config.nave_limite
        
        # Pontuação atual
        self.pontuacao = 0
        
        # Nivel atual
        self.nivel = 1
