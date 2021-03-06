import pygame
import random
import time
from os import path

#diretorios de imagem e som
img_dir = path.join(path.dirname(__file__), 'sprites')

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
aceleracao = -0.05
H = 130

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
       self.image = pygame.transform.scale(player_img, (45, 45))   
       self.image.set_colorkey(BLACK)   
       self.rect = self.image.get_rect()

       #posicoes
       self.rect.y = HEIGHT/2
       self.rect.x = (WIDTH/2)-30
       #raio
       self.radius = 25

       self.speedx = 0 

       self.speedy = 2

       self.state = FALLING



   def update(self):
       self.rect.y += self.speedy 
       if self.rect.y <= 0:
           self.rect.y = 0
           self.speedy = 0 
           self.state = STILL
       self.speedy += gravidade


class Cano_de_cima (pygame.sprite.Sprite):

   def __init__(self, canodecima,x):

       pygame.sprite.Sprite.__init__(self)

       #define a largura aleatoria do cano
       aleatorio = random.randint(100,350)

       self.image = pygame.transform.scale(canodecima, (80, 600))       
       self.rect = self.image.get_rect()

       #poscicoes 
       self.rect.bottom =  aleatorio
       self.rect.x = x

       self.speedx = -4.5
       self.speedy = 0 

       #somado
       self.somado = False

   #def update(self):
   def update(self):
       self.rect.x += self.speedx 
       if self.speedx > -4.5:
           self.speedx = -4.5



class Cano_de_baixo (pygame.sprite.Sprite):

   def __init__(self,canodebaixo,x,y):

       pygame.sprite.Sprite.__init__(self)

       #altura do cano aleatoria


       self.image = pygame.transform.scale(canodebaixo, (80, 600))       
       self.rect = self.image.get_rect()

       #posicao
       self.rect.top = y
       self.rect.x = x

       self.speedx = -4.5
       self.speedy = 0

       #somadao
       self.somado = False
   #def update(self):
   def update(self):
       self.rect.x += self.speedx 
       if self.speedx > -4.5:
           self.speedx = -4.5 




class Base(pygame.sprite.Sprite): 

   def __init__(self,base,x,y):

       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.transform.scale(base,(9999,150))
       self.image.set_colorkey(BLACK)
       self.rect = self.image.get_rect()

       # posicao 
       self.rect.x = x
       self.rect.y = y

       #velocidade
       self.speedx = -4.5
       self.speedy = 0 

   def update(self):
       self.rect.x += self.speedx 

class Telainicial(pygame.sprite.Sprite):

   def __init__(self,inicio,x,y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.transform.scale(inicio,(350,300))
       self.image.set_colorkey(BLACK)
       self.rect  = self.image.get_rect()

       #posicao
       self.rect.x = x 
       self.rect.y = y

       self.speedy = 0

   def update(self):
       self.speedy += 0

class Game_over(pygame.sprite.Sprite):

   def __init__(self,gameover,x,y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.transform.scale(gameover,(350,300))

       self.rect = self.image.get_rect()

       self.rect.x = x 
       self.rect.y = y   


def load_assets(img_dir):
   assets = {}
   assets["jod1"] = pygame.image.load(path.join(img_dir, "jod.png")).convert_alpha()
   assets["canodecima"] = pygame.image.load(path.join(img_dir, "upper_pipe_img.png")).convert_alpha()
   assets['canodebaixo']=pygame.image.load(path.join(img_dir, "lower_pipe_img.png")).convert_alpha()
   assets['barulho_pulo']=pygame.mixer.Sound(path.join(img_dir, 'swoosh.wav'))
   assets['background']=pygame.image.load(path.join(img_dir, "backgroundnovo.png")).convert_alpha()
   assets['barulho_pulo']=pygame.mixer.Sound(path.join(img_dir, 'swoosh.wav')) 
   assets['base'] = pygame.image.load(path.join(img_dir, "base.png"))
   assets['hit'] = pygame.mixer.Sound(path.join(img_dir, 'hit.wav'))
   assets['score0'] = pygame.image.load(path.join(img_dir, "0.png")).convert_alpha()
   assets['score1'] = pygame.image.load(path.join(img_dir, "1.png")).convert_alpha()
   assets['score2'] = pygame.image.load(path.join(img_dir, "2.png")).convert_alpha()
   assets['score3'] = pygame.image.load(path.join(img_dir, "3.png")).convert_alpha()
   assets['score4'] = pygame.image.load(path.join(img_dir, "4.png")).convert_alpha()
   assets['score5'] = pygame.image.load(path.join(img_dir, "5.png")).convert_alpha()
   assets['score6'] = pygame.image.load(path.join(img_dir, "6.png")).convert_alpha()
   assets['score7'] = pygame.image.load(path.join(img_dir, "7.png")).convert_alpha()
   assets['score8'] = pygame.image.load(path.join(img_dir, "8.png")).convert_alpha()
   assets['score9'] = pygame.image.load(path.join(img_dir, "9.png")).convert_alpha()   
   assets['point'] = pygame.mixer.Sound(path.join(img_dir, 'point.wav'))
   assets['inicio'] = pygame.image.load(path.join(img_dir, "inicio.png")).convert_alpha()   
   assets['jod2'] = pygame.image.load(path.join(img_dir, "jod2.png")).convert_alpha()
   assets['jod3'] = pygame.image.load(path.join(img_dir, "jod3.png")).convert_alpha()
   assets['jod4'] = pygame.image.load(path.join(img_dir, "jod4.png")).convert_alpha()
   assets['jod5'] = pygame.image.load(path.join(img_dir, "jod5.png")).convert_alpha()
   assets['jod6'] = pygame.image.load(path.join(img_dir, "jod6.png")).convert_alpha()
   assets['jod7'] = pygame.image.load(path.join(img_dir, "jod8.png")).convert_alpha()
   assets['jod9'] = pygame.image.load(path.join(img_dir, "jod9.png")).convert_alpha()
   assets['Canodecima1'] = pygame.image.load(path.join(img_dir, "Canodecima1.png")).convert_alpha()
   assets['Canodebaixo1'] = pygame.image.load(path.join(img_dir, "Canodebaixo1.png")).convert_alpha()
   assets['background1'] = pygame.image.load(path.join(img_dir, "background1.png")).convert_alpha()
   assets['gameover1'] = pygame.image.load(path.join(img_dir, "gameover1.png")).convert_alpha()
   assets['telainicial1'] = pygame.image.load(path.join(img_dir, "telainicial1.png")).convert_alpha()
   assets['jodpulando'] = pygame.image.load(path.join(img_dir, "jodpulando.png")).convert_alpha()
   assets['femalejod'] = pygame.image.load(path.join(img_dir, "femaleJod.png")).convert_alpha()
   assets['chooseyourskin'] = pygame.image.load(path.join(img_dir, "chooseyourskin.png")).convert_alpha()
   assets['canodebaixoflappy'] = pygame.image.load(path.join(img_dir, "canodebaixoflappy.png")).convert_alpha()
   assets['canodecimaflappy'] = pygame.image.load(path.join(img_dir, "canodecimaflappy.png")).convert_alpha()
   return assets


#funcao que faz o score 
class Score (pygame.sprite.Sprite):
   def __init__(self, scoreinicial,x,y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.transform.scale(scoreinicial,(60,80))
       self.image.set_colorkey(BLACK)
       self.rect = self.image.get_rect()

       self.rect.x = x 
       self.rect.y = y 


#def HighScore(screen):
class Jumping (pygame.sprite.Sprite):
   def __init__(self,jod,x,y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.transform.scale(jod,(45,45))
       self.image.set_colorkey(BLACK)
       self.rect = self.image.get_rect()

       self.rect.x = x 
       self.rect.y = y 

#choose your skin sprite
class ChooseSkin(pygame.sprite.Sprite):
   def __init__(self, femalejod,x,y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.transform.scale(femalejod,(200,100))
       self.image.set_colorkey(BLACK)
       self.rect = self.image.get_rect()

       self.rect.x = x
       self.rect.y = y


def game_screen(screen):
   contador =0
   proximo = 1
   
   assets = load_assets(img_dir)

   clock = pygame.time.Clock()

   background = assets["background1"]
   background = pygame.transform.scale(background,(WIDTH,HEIGHT+20))
   background_rect = background.get_rect()

   #cria o passaro
   all_sprites = pygame.sprite.Group()
   classeplayer = pygame.sprite.Group()
   #randomiza a escolha do sprite(jod)
   player = Player(assets["jod1"])
   all_sprites.add(player)
   classeplayer.add(player)
   
   #Cria a base
   classebase = pygame.sprite.Group()
   base = Base(assets['base'],0,HEIGHT-100)
   all_sprites.add(base)
   classebase.add(base)
   #segundabase
   base2 = Base(assets['base'],1000,HEIGHT-100)
   all_sprites.add(base2)
   classebase.add(base2)

   #cria os canos
   canos = pygame.sprite.Group()
   #Canodecima1
   canodecima = Cano_de_cima(assets['canodecima'], (WIDTH/2)+250)
   all_sprites.add(canodecima)
   canos.add(canodecima)
   #Canodebaixo1 
   canodebaixo = Cano_de_baixo(assets['canodebaixo'], (WIDTH/2)+250,canodecima.rect.bottom+H)
   all_sprites.add(canodebaixo)
   canos.add(canodebaixo)
    #Canodecima2
   canodecima2 = Cano_de_cima(assets['canodecima'], (WIDTH/2)+550)
   all_sprites.add(canodecima2)
   canos.add(canodecima2)
   #Canodebaixo2
   canodebaixo2 = Cano_de_baixo(assets['canodebaixo'],(WIDTH/2)+550, canodecima2.rect.bottom+H)
   all_sprites.add(canodebaixo2)
   canos.add(canodebaixo2)
   #canodecima3
   canodecima3 = Cano_de_cima(assets['canodecima'], (WIDTH/2)+850)
   all_sprites.add(canodecima3)
   canos.add(canodecima3)
   #Canodebaixo3
   canodebaixo3 = Cano_de_baixo(assets['canodebaixo'],(WIDTH/2)+850, canodecima3.rect.bottom+H)
   all_sprites.add(canodebaixo3)
   canos.add(canodebaixo3)

   #adiciona a base


   #adiciona  os scores
   scores = pygame.sprite.Group()
   score0 = Score(assets['score0'], WIDTH/2,(HEIGHT/2)-250)
   scores.add(score0)
   all_sprites.add(score0)

   #estados
   PLAYING = 0
   DONE = 1
   INICIO = 2
   GAME_OVER = 3 
   state = INICIO

   telainicial = pygame.sprite.Group()

   while state != DONE: 
       clock.tick(FPS)

       if state == INICIO:
           player.speedy = STILL
           inicial = Telainicial(assets['telainicial1'], 10, (HEIGHT/2)-250)
           inicial2 = ChooseSkin(assets['chooseyourskin'], 150,(HEIGHT-300))
           telainicial = pygame.sprite.Group()
           telainicial.add(inicial2)
           telainicial.add(inicial)
           telainicial.draw(screen)
           telainicial.update()
           pygame.display.flip()
           canodecima.speedx = 0
           canodebaixo.speedx = 0 
           canodecima2.speedx = 0
           canodebaixo2.speedx = 0 
           canodecima3.speedx = 0
           canodebaixo3.speedx = 0 
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RIGHT:
                       for p in classeplayer:
                           p.kill()
                       jogador = "jod{0}".format(proximo+1)
                       player = Player(assets[jogador])
                       all_sprites.add(player)
                       classeplayer.add(player)
                       proximo += 1
                       if proximo >= 5:
                           proximo =  1
                   if event.key == pygame.K_LEFT:
                       for p in classeplayer:
                           p.kill()
                       player = Player(assets['femalejod'])
                       all_sprites.add(player)
                       classeplayer.add(player)
                   if event.key == pygame.K_SPACE:
                       del telainicial
                       state = PLAYING
                       player.speedy = FALLING


       if state == PLAYING:
           for event in pygame.event.get():
               #adiciona o quit
               if event.type == pygame.QUIT:
                   state = DONE

               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_SPACE:
                       player.speedy = -12.5
                       assets['barulho_pulo'].play()



       if len(canos)<4 and state == PLAYING:

           novo_cano_de_cima = Cano_de_cima(assets['canodecima'],(WIDTH/2)+350)        
           novo_cano_de_baixo = Cano_de_baixo(assets['canodebaixo'], (WIDTH/2)+350, novo_cano_de_cima.rect.bottom+H)
           canos.add(novo_cano_de_cima)
           canos.add(novo_cano_de_baixo)
           all_sprites.add(novo_cano_de_cima)
           all_sprites.add(novo_cano_de_baixo)


       for i in canos:
          if i.rect.right<0 and state == PLAYING:
              i.kill()
          if i.rect.right<=player.rect.x and i.somado==False:
              contador += 0.5
              i.somado=True
              for s in scores:
                  s.kill()
              if contador%1==0:
                  numeros=str(int(contador))
                  digitos=0


                  for z in numeros:

                      if digitos==0:
                          x=WIDTH/2
                          y=(HEIGHT/2)-250
                      else:
                          x=WIDTH/2 - 90
                          y=(HEIGHT/2)-250

                      
                      img_name = "score{0}".format(numeros[len(numeros)-(digitos+1)])
                      score1 = Score(assets[img_name], x,y)
                      scores.add(score1)
                      all_sprites.add(score1)
                      assets['point'].play()
                      digitos+=1 


       for base1 in classebase:
           if base1.rect.centerx == 380:
               nova_base = Base(assets['base'],0,HEIGHT-100)
               classebase.add(nova_base)
               all_sprites.add(nova_base)


       if state == PLAYING:          
           hit = pygame.sprite.groupcollide(canos, classeplayer, False,False)
           hit2 = pygame.sprite.groupcollide(classebase,classeplayer,False, False)

           if len(hit)!= 0:
               assets['hit'].play()
               player.kill()
               state = GAME_OVER


           if len(hit2)!= 0:
               assets['hit'].play()
               player.kill()
               state = GAME_OVER


       if state == GAME_OVER:
           game_over = Game_over(assets['gameover1'],50,(WIDTH/2)-100)
           all_sprites.add(game_over)
           for i in canos:
               i.kill()
           if contador < 10:
               for s in scores:
                   s.kill()                   
               strcont = str(int(contador))
               img = "score{0}".format(strcont)
               newscore = Score(assets[img],100,(WIDTH/2+100))
               all_sprites.add(newscore)
           elif contador >= 10:
               for s  in scores:
                   s.kill()
               strcont = str(int(contador))
               primeirodigito = strcont[0]
               segundodigito = strcont[1]
               x1= 100
               y1 = (WIDTH/2)+100
               x2 = 170
               y2 = (WIDTH/2)+100
               img1 = "score{0}".format(primeirodigito)
               img2 = "score{0}".format(segundodigito)
               scorefinal1 = Score(assets[img1], x1,y1)
               scorefinal2 = Score(assets[img2],x2,y2)
               all_sprites.add(scorefinal1)
               all_sprites.add(scorefinal2)
               scores.add(scorefinal1)
               scores.add(scorefinal2)
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_SPACE:
                       state = DONE


       all_sprites.update()
       screen.fill(BLACK)
       screen.blit(background, background_rect)
       all_sprites.draw(screen)
       pygame.display.flip()

# Inicialização do Pygame
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("JodVentures")


try:
   game_screen(screen)
finally:
   pygame.quit()