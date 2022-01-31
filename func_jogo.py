import sys
import pygame
from bala import Bala
from alien import Alien
from time import sleep

def checa_evento_KEYDOWN(nave, event, tela, balas, config):
    """Checa eventos de keydown"""
    if event.key == pygame.K_RIGHT:
        nave.movendo_direita = True
    elif event.key == pygame.K_LEFT:
        nave.movendo_esquerda = True
    elif event.key == pygame.K_SPACE:
        disparar(nave, tela, balas, config)
    elif event.key == pygame.K_q:
        sys.exit()
            
def checa_evento_KEYUP(nave, event):
    """Checa eventos de keyup"""
    if event.key == pygame.K_RIGHT:
        nave.movendo_direita = False
    elif event.key == pygame.K_LEFT:
        nave.movendo_esquerda = False
            
def checa_evento(pontuacao, nave, config, tela, balas, 
                 botao_play, status, aliens):
    """Laço que checa eventos durante o jogo"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            checa_evento_KEYDOWN(nave, event, tela, balas, config)
            
        elif event.type == pygame.KEYUP:
            checa_evento_KEYUP(nave, event)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            checa_botao_play(pontuacao, config, tela, nave, 
                             aliens, balas, status, botao_play, 
                             mouse_x, mouse_y)
                
def checa_botao_play(pontuacao, config, tela, nave, aliens, balas, status,
                     botao_play, mouse_x, mouse_y):
    """Inicia o jogo ao clicar no botao play"""
    clique = botao_play.rect.collidepoint(mouse_x, mouse_y)
    if clique and not status.jogo_ativo:
        # Restaura as velocidades iniciais do jogo
        config.init_config_dinamica()
        
        # Oculta o mouse
        pygame.mouse.set_visible(False)
        
        # Reinicia os dados estatísticos do jogo
        status.reset_status()
        status.jogo_ativo = True
        
        # Reinicia as imagens do painel de pontuações
        pontuacao.prep_pontuacao()
        pontuacao.prep_pontuacao_maxima()
        pontuacao.prep_nivel()
        pontuacao.prep_naves()
        
        # Esvazia aliens e balas
        aliens.empty()
        balas.empty()
        
        # Centraliza a nave e cria nova frota
        nave.centraliza()
        cria_frota(config, tela, aliens, nave)
    
def checa_pont_max(status, pontuacao):
    """Checa se há uma nova pontuação máxima"""
    if status.pontuacao > status.pontuacao_maxima:
        status.pontuacao_maxima = status.pontuacao
        pontuacao.prep_pontuacao_maxima()
        
def atualiza_tela(nave, config, tela, balas, 
                  aliens, botao_play, status, pontuacao):
    """Redesenha a tela a cada passagem pelo laço"""
    # Preenche a cor de fundo da tela
    tela.fill(config.background_cor)
    
    # Redesenha todos os projéteis atrás da espaçonave e dos
    # alienígenas
    for bala in balas:
        bala.drawme()
        
    # Desenha a nave na parte inferior central da tela
    nave.blitme()
    
    # Desenha a frota de aliens
    aliens.draw(tela)
    
    # Desenha a informação sobre pontuação
    pontuacao.mostra_pontuacao()
    
    # Desenha o botão Play se o jogo estiver inativo
    if not status.jogo_ativo:
        botao_play.draw_botao()
        
    # Deixa a tela mais recente visível
    pygame.display.flip()
    
    
def atualiza_bala(balas, aliens, config, tela, nave, status, pontuacao):
    """"
    Atualiza a posição dos projéteis e se livra dos projéteis
    antigos.
    """
    # Atualiza a posição dos projéteis
    balas.update()
            
    # Livra-se dos projéteis antigos
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)
            
    # Checa colisões entre alienígenas e projéteis
    checa_alien_bala_colisoes(balas, aliens, config, tela, 
                              nave, status, pontuacao)
            
def checa_alien_bala_colisoes(balas, aliens, config, tela, 
                              nave, status, pontuacao):
    """Responde a colisões entre aliens e os projéteis"""
    # Verifica se algum projétil atingiu os alienígenas
    # Em caso afirmativo, livra-se do projétil e do alienígena
    collisions = pygame.sprite.groupcollide(balas, aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            status.pontuacao += config.alien_pontos * len(aliens)
            pontuacao.prep_pontuacao()
        checa_pont_max(status, pontuacao)
    
    if len(aliens) == 0:
        # Se a frota toda for destruída, inicia um novo nível
        balas.empty()
        config.aumenta_velocidade()
        
        # Aumenta o nível
        status.nivel += 1
        pontuacao.prep_nivel()
        
        cria_frota(config, tela, aliens, nave)
            

def disparar(nave, tela, balas, config):
    """"Dispara um projétil se o limite ainda não foi alcançado."""
    # Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(balas) < config.bala_limite:
        nova_bala = Bala(tela, config, nave)
        balas.add(nova_bala)
        
    
def pega_numero_linhas(config, nave_height, alien_height):
    """
    Determina o número de linhas de aliens que cabem na tela
    """
    y_disponivel = (config.tela_fundo[1] 
                    - nave_height 
                    - (3 * alien_height))
                    
    numero_linhas = int(y_disponivel / (2 * alien_height))
    
    return numero_linhas
        
def pega_numero_alien_x(config, alien_largura):
    """Determina o número de alienígenas que cabem em uma linha."""
    x_disponivel = config.tela_fundo[0] - 2 * alien_largura
    numero_alien_x = int(x_disponivel / (2 * alien_largura))
    
    return numero_alien_x
    
    
def cria_alien(config, tela, aliens, numero_alien, numero_linha):
    """Cria um alienígena e o posiciona na linha"""
    alien = Alien(tela, config)
    alien_largura = alien.rect.width
    alien_altura = alien.rect.height
    alien.x = alien_largura + (2 * alien_largura * numero_alien)
    alien.y = alien_altura + (2 * alien_altura * numero_linha)
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)
    
def cria_frota(config, tela, aliens, nave):
    """Cria uma frota completa de alienígenas"""
    # Determina o número de aliens por linha e o número de linhas
    alien = Alien(tela, config)
    numero_alien_x = pega_numero_alien_x(config, alien.rect.width)
    numero_linhas = pega_numero_linhas(config, nave.rect.height, 
                                       alien.rect.height)
    
    # Cria as linhas de alienígenas
    for numero_linha in range(numero_linhas):
        for numero_alien in range(numero_alien_x):
            cria_alien(config, tela, aliens, numero_alien, numero_linha)
     
def muda_direcao_frota(aliens, config):
    """Faz toda a frota descer e muda a sua direção."""
    for alien in aliens.sprites():
        alien.rect.y += config.frota_velocidade_y
        
    config.frota_direcao *= -1
    
def checa_frota_canto(aliens, config):
    """
    Responde apropriadamente se algum alienígena alcançou uma
    borda.
    """
    for alien in aliens.sprites():
        if alien.checa_canto():
            muda_direcao_frota(aliens, config)
            break
        
def nave_hit(config, status, tela, nave, aliens, balas, pontuacao):
    """
    Responde quando a nave for atingida por um alienígena
    """
    # Decrementa naves_restantes
    status.naves_restantes -= 1
    
    # Altera a pontuação de naves restantes
    pontuacao.prep_naves()
    
    # Esvazia o grupo de alinígenas e de projéteis
    aliens.empty()
    balas.empty()
    
    # Cria uma nova frota e centraliza a nave
    cria_frota(config, tela, aliens, nave)
    nave.centraliza()
    
    # Faz uma pausa no jogo
    sleep(0.5)
        
    if status.naves_restantes == 0:
        status.jogo_ativo = False
        pygame.mouse.set_visible(True)
        

def checa_alien_chao(config, status, tela, nave, aliens, balas, pontuacao):
    """Verifica se o alien tocou o chão"""
    tela_rect = tela.get_rect()
    
    for alien in aliens.sprites():
        if alien.rect.bottom >= tela_rect.bottom:
            nave_hit(config, status, tela, nave, aliens, balas, pontuacao)
            break
    
def atualiza_aliens(aliens, config, nave, tela, balas, status, pontuacao):
    """"Atualiza a posição dos aliens"""
    checa_frota_canto(aliens, config)
    aliens.update()
    
    # Verifica se houve colisões entre alienígenas e a nave
    if pygame.sprite.spritecollideany(nave, aliens):
        nave_hit(config, status, tela, nave, aliens, balas, pontuacao)
        
    # Verifica se algum alinégena tocou o chão
    checa_alien_chao(config, status, tela, nave, aliens, balas, pontuacao)
    

    
        