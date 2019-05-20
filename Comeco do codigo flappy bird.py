#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:48:52 2019

@author: digomattar
"""

import pygame
import random
import time
from os import path

#diretorios de imagem e som
img_dir = path.join(path.dirname(__file__), 'sprites')
snd_dir = path.join(path.dirname(__file__), 'snd')
fnt_dir = path.join(path.dirname(__file__), 'font')

WIDTH = 380 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # F

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Constantes
gravidade = 2
GROUND = HEIGHT*5//6
velocidadecano = -4
aceleracao = 0.5

#3 possiveis estados do 
STILL =0
JUMPING = 1
FALLING = 2
#classe do passaro
class Player(pygame.sprite.Sprite):
    
    def __init__(self, player_img):
        #construtor e coletar imagem 
        pygame.sprite.Sprite.__init__(self)    
        self.image = player_img      
        self.image = pygame.transform.scale(player_img, (35, 35))   
        self.image.set_colorkey(BLACK)   
        self.rect = self.image.get_rect()
        
        #posicoes
        self.rect.y = HEIGHT/2
        self.rect.x = (WIDTH/2)-30
        #raio
        self.radius = 25
        
        self.speedx = 0 
        
        self.speedy = FALLING
        
        self.state = FALLING
        
        
        
    def update(self):
        self.rect.y += self.speedy 
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.speedy = 0 
            self.state = STILL
        if self.rect.y <= 0:
            self.rect.y = 0
            self.speedy = 0 
            self.state = STILL
        self.speedy += gravidade
        
        
class Cano_de_cima (pygame.sprite.Sprite):
    
    def __init__(self, canodecima):
        
        pygame.sprite.Sprite.__init__(self)
        
        #define a largura aleatoria do cano
        aleatorio = random.randint(100,250)
        
        self.image = pygame.transform.scale(canodecima, (80, aleatorio))       
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
        #poscicoes 
        self.rect.y =  0
        self.rect.x = (WIDTH/2)+25
        
        self.speedx = -5
        self.speedy = 0 
        
    #def update(self):
    def update(self):
        self.rect.x += self.speedx + aceleracao
        if self.speedx > -15:
            self.speedx = -15 
        if self.rect.x < 0:
            self.kill()
            

class Cano_de_baixo (pygame.sprite.Sprite):

    def __init__(self,canodebaixo):
        
        pygame.sprite.Sprite.__init__(self)
        
        #altura do cano aleatoria
        aleatorio = random.randint(100,250)
        
        self.image = pygame.transform.scale(canodebaixo, (80, aleatorio))       
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
        #posicao
        self.rect.y = HEIGHT-150
        self.rect.x =(WIDTH/2)+25
        
        self.speedx = -5
        self.speedy = 0
        
    #def update(self):
    def update(self):
        self.rect.x += self.speedx + aceleracao
        if self.speedx > -15:
            self.speedx = -15 
        if self.rect.x < 0:
            self.kill()
            
        
            
class Base(pygame.sprite.Sprite): 
          
    def __init__(self,base):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(base,(10000,100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
        # posicao 
        self.rect.x = 0
        self.rect.y = HEIGHT-100
        
        #velocidade
        self.speedx = -5
        self.speedy = 0 
        
    def update(self):
        self.rect.x += self.speedx + aceleracao
        if self.speedx > -15:
            self.speedx = -15 
            


def load_assets(img_dir, snd_dir, fnt_dir):
    assets = {}
    assets["player_img"] = pygame.image.load(path.join(img_dir, "yellowbird-upflap.png")).convert()
    assets["canodecima"] = pygame.image.load(path.join(img_dir, "upper_pipe_img.png")).convert()
    assets['canodebaixo']=pygame.image.load(path.join(img_dir, "lower_pipe_img.png")).convert()
    assets['barulho_pulo']=pygame.mixer.Sound(path.join(img_dir, 'swoosh.wav')) 
    assets['background']=pygame.image.load(path.join(img_dir, "background-day.png")).convert()
    assets['barulho_pulo']=pygame.mixer.Sound(path.join(img_dir, 'swoosh.wav')) 
    assets['base'] = pygame.image.load(path.join(img_dir, "base.png")).convert()
    assets['hit'] = pygame.mixer.Sound(path.join(img_dir, 'hit.wav'))
    return assets

def game_screen(screen):
    
    assets = load_assets(img_dir, snd_dir, fnt_dir)
                         
    clock = pygame.time.Clock()
    
    background = assets["background"]
    #background.image = pygame.transform.scale(background(WIDTH,HEIGHT))
    background_rect = background.get_rect()
    
    #cria o passaro
    player = Player(assets["player_img"])
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    canodebaixo = Cano_de_baixo(assets['canodebaixo'])

    all_sprites.add(canodebaixo)
    
    canodecima = Cano_de_cima(assets['canodecima'])
    all_sprites.add(canodecima)
    
    base = Base(assets['base'])

    all_sprites.add(base)
    
    
    
    PLAYING = 0

    DONE = 1

    state = PLAYING
    while state != DONE:
        
        clock.tick(FPS)
        
        
        if state == PLAYING:
            for event in pygame.event.get():
                #adiciona o quit
                if event.type == pygame.QUIT:
                    state = DONE
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.speedy = -15
                        assets['barulho_pulo'].play()
                        
        #if state == PLAYING:
            
            #for canodebaixo.rect.x in range(0,1):
               # all_sprites.add(canodebaixo)
                
        #if state == PLAYING:          
         #   hit1 = pygame.sprite.spritecollide(canodecima, player, False)
          #  hit2 = pygame.sprite.spritecollide(canodebaixo, player, False)
           # 
            #if hit2 or hit1:
             #   assets['hit'].play()
              #  player.kill()
               # state = DONE
                
            
            
        all_sprites.update()
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        pygame.display.flip()
        

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Flappy_Bird")
        

try:
    game_screen(screen)
finally:
    pygame.quit()


        
        
        
        
        