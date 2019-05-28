#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:08:17 2019

@author: digomattar
"""
import random
from tkinter import *
#Flappy bird game 
xcair = 10
altura = 600
largura = 400
# Classes
class passaro:
    def __init__(self,vEsq,vVert):
        #Posicao e velocidade
        self.y = altura/2
        self.vEsq = velopassaroEsq
        self.vVert = velopassaroVert
        self.up = 0
        
    def paraCima(self):
        if(self.up > 0):
            self.up -= 1
            self.y -= vVert
            
    def paraBaixo(self):
        if (self.up ==0):
            self.y -= cair
            
class cano:
    def __init__(self,largura,espaco,x):
        self.x = x
        self.largura = largura
        self.altura  = random.randint(50,300)
        self.espaco = espaco
        self.pontuacao=  1
        
    def percorre(self, vEsq):
        self.x -= vEsq
        
    def canodecima(self):
        return [self.x,0,self.x+self.largura,0,self.x+self.largura,self.altura,self.x,self.altura]
    
    def canodebaixo(self):
        return [self.x,self.altura+self.espaco,self.x+self.largura,self.altura+self.espaco,self.x+self.largura,altura,self.x,altura]
    
    def espacodomeio(self):
        return[self.x,self.altura,self.x+self.largura,self.altura,self.x+self.largura,self.altura+self.espaco,self.x,self.A+self.espaco]
        

#classe do jogo, criando a tela
class jogo:
    def __init__(self):
        self.tela = Tk()
        self.c = Canvas(self.janela,altura1 = altura, largura1 = largura, bg='blue')
        self.passaro(10,10)
        self.cano(30, 150, largura)
        
        
        
    
        
        
        
        
        
    def comeca(self):
        while(True):
            self.c.delete('all')
            
            self.janela.uptdate_pygame()
            self.janela.update(30)
        
        
            
 