import pygame.mixer

class Som():
    """Classe responsável por administrar os sons do jogo."""

    def __init__(self):
        self.diretorio = 'sons/'
        self.sfx = ['disparar', 'game_over', 'nave_hit']
        self.music = ['hard_stage']
        self.format = '.mp3'

    def play_sfx(self, index):
        """Toca um sfx de acordo com o indice de Som.sfx"""
        efeito = pygame.mixer.Sound(self.diretorio + self.sfx[index] + self.format)
        pygame.mixer.Sound.play(efeito)

    def play_music(self, index):
        """Toca uma musica de acordo com o indice de Som.music"""
        pygame.mixer.music.load(self.diretorio + self.music[index] + self.format)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        """Para de tocar a musica de fundo"""
        pygame.mixer.music.stop()

