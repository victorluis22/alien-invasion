import json

class JogoStatus():
    """Armazena dados estatísticos do jogo"""
    
    def __init__(self, config):
        self.config = config
        
        # Flag que indica que o jogo está ativo
        self.jogo_ativo = False
        
        # Pontuação máxima
        self.pontuacao_maxima = self.pega_pontuacao_maxima()

        self.reset_status()

    def pega_pontuacao_maxima(self):
        """
        Verifica se há um histórico de pontuação máxima. Se não retorna 0.
        """ 
        try:
            with open('pontuacao_maxima.json') as arquivo_json:
                pontos = int(json.load(arquivo_json))
        except FileNotFoundError:
            pontos = 0

        return pontos

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
