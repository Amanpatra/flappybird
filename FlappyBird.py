# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:12:02 2019

@author: shyan
"""

import pygame
import random

pygame.init()

w=600
h=512
x=100
y=100
jump=0
vel=10
score=0
restart=0

white=(255,255,255)
black=(0,0,0)
run1=True
run2=True
run3=True
Font=pygame.font.SysFont('times new roman',20,True,True)
Font2=pygame.font.SysFont('Ariel',35,False,False)

screen=pygame.display.set_mode((w,h))

Bimg=[]
Pimg=[]
for i in range(3):
    img=pygame.image.load('D:\\Python programs\\FB\\bird{}.png'.format(i))
    Bimg.append(img)

for i in range(2):
    img=pygame.image.load('D:\\Python programs\\FB\\pipe{}.png'.format(i))
    Pimg.append(img)
    
GOimg=pygame.image.load('D:\\Python programs\\FB\\gameover.png')
FRONTimg=pygame.image.load('D:\\Python programs\\FB\\message.png')
BGimg=pygame.image.load('D:\\Python programs\\FB\\BG.png')

class bird:
    def __init__(self):
        self.count=-1
        self.angle=0
    def disp(self):
        self.count+=1
        if self.count==6:
            self.count=0

        if jump>2:
            self.angle=30
        elif jump>0:
            self.angle=15
        elif jump<-2:
            self.angle=330
        elif jump<0:
            self.angle=345
        else:
            self.angle=0
        new_Bimg=pygame.transform.rotate(Bimg[self.count//2],self.angle)
        screen.blit(new_Bimg,(x,y))
Bobj=bird()

class obs:
    def __init__(self):
        self.xpos=[800,900,1000,1100,1200,1300,1400,1500,1600]
        self.y1=random.randint(300,380)
        self.x1=random.choice(self.xpos)
        self.s=random.randint(0,1)
        self.yp=self.y1-random.randint(400,500)
    def change(self):
        self.x1-=vel
        if self.x1<-100 or restart==1:
            self.x1=random.choice(self.xpos)
            self.y1=random.randint(200,380)
            self.yp=self.y1-random.randint(400,500)
            self.s=random.randint(0,1)
    def display(self):
        screen.blit(Pimg[self.s],(self.x1,self.y1))
        new_Pimg=pygame.transform.rotate(Pimg[self.s],180)
        screen.blit(new_Pimg,(self.x1,self.yp))
    def checkcollide(self):
        global run2
        if x+24>=self.x1+2 and x+24<self.x1+50:
            if y>=self.y1 and y<=self.y1+320:
                run2=False
            elif y+2>=self.yp and y+2<=self.yp+320:
                run2=False
        elif x+34>=self.x1+2 and x+34<=self.x1+50:
            if y+16>=self.y1 and y+16<=self.y1+320:
                run2=False
            elif y+16>=self.yp and y+16<=self.yp+320:
                run2=False
        elif x+32>=self.x1+2 and x+32<=self.x1+50:
            if y+20>=self.y1 and y+20<=self.y1+320:
                run2=False
            elif y+20>=self.yp and y+20<=self.yp+320:
                run2=False
        elif x+20>=self.x1+2 and x+20<=self.x1+50:
            if y+24>=self.y1 and y+24<=self.y1+320:
                run2=False
            elif y+24>=self.yp and y+24<=self.yp+320:
                run2=False
        elif x+10>=self.x1+2 and x+10<=self.x1+50:
            if y+24>=self.y1 and y+24<=self.y1+320:
                run2=False
            elif y+24>=self.yp and y+24<=self.yp+320:
                run2=False      
    def call(self):
        obs.change(self)
        obs.checkcollide(self)
        obs.display(self)
    
ob1=obs()
ob2=obs()
ob3=obs()

while True:    
    x=100
    y=100
    jump=0
    vel=10
    score=0
    run1=True
    run2=True
    run3=True
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

    while run1:    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        k=pygame.key.get_pressed()
        if k[pygame.K_SPACE]:
            run1=False
        screen.fill(white)
        screen.blit(FRONTimg,(208,120))
        pygame.display.update()
        
    while run2:
        restart+=1
        pygame.time.delay(40)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
    
        if jump<-7:
            jump=-7
        neg=1
        if jump<0:
            neg=-1
        y-=int((jump**2)*0.5*neg)
        jump-=1
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            jump=6
        if y<-6:
            y=-5
        elif y>478:
            run2=False
        
        screen.blit(BGimg,(0,0))
        screen.blit(BGimg,(284,0))
        screen.blit(BGimg,(568,0))
        Bobj.disp()
        ob1.call()
        ob2.call()
        ob3.call()
        text=Font.render("Score " + str(score),True,black)
        screen.blit(text,(500,2))
        score+=1
        if score%500==0:
            vel+=2
                
        pygame.display.update()
        
    while run3:
        pygame.time.delay(40)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        k=pygame.key.get_pressed()
        if k[pygame.K_r]:
            run3=False
        screen.blit(GOimg,(204,200))
        text=Font2.render("press \"r\" to restart",True,black)
        screen.blit(text,(200,250))
    
        pygame.display.update()
    restart=0
    pygame.display.update()