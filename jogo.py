import pygame
from pygame.sprite import Group
import func_jogo as fj
from config import Configuracoes
from nave import Nave
from jogo_status import JogoStatus
from botao import Botao
from pontuacao import Pontuacao

def run_game():
    # Inicializa o jogo
    pygame.init()

    
    # Cria um objeto para administrar as configurações
    # Cria um objeto para administrar a tela
    # Determina o nome do programa
    config = Configuracoes()
    tela = pygame.display.set_mode(config.tela_fundo)
    pygame.display.set_caption("Alien Invasion")
    
    # Cria objetos importantes para o jogo
    nave = Nave(config, tela)
    balas = Group()
    aliens = Group()
    status = JogoStatus(config)
    botao_play = Botao(tela, config, 'Jogar')
    pontuacao = Pontuacao(tela, config, status)
    
    # Cria a frota de alienígenas
    fj.cria_frota(config, tela, aliens, nave)

    # Inicia o laço principal do jogo
    while True:
        #Observa eventos de teclado e de mouse
        fj.checa_evento(pontuacao, nave, config, tela,
                        balas, botao_play, status, aliens) 
        
        if status.jogo_ativo:
            # Atualiza a posição da nave
            nave.atualiza()
            
            # Atualiza a posição da bala
            fj.atualiza_bala(balas, aliens, config, tela, 
                             nave, status, pontuacao)
            
            # Atualiza a posição dos alienígenas
            fj.atualiza_aliens(aliens, config, nave, 
                               tela, balas, status, pontuacao)
            
        # Atualiza a tela
        fj.atualiza_tela(nave, config, tela, balas, 
                         aliens, botao_play, status, pontuacao)
            
        
        
run_game()
