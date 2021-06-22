
from typing import Text
import pygame, sys
from pygame import image
from pygame.locals import *

#janela
print("Rodando")
pygame.init()
print("Abriu")
screen = pygame.display.set_mode((600, 600))

#titulo da janela
pygame.display.set_caption( 'QUIZ AMÉRICA LATINA' )

#ícone da janela
image7 = pygame.image.load('images/icon.png')
pygame.display.set_icon(image7)

#cores
azulfundo = (0, 0, 102)
azulcirculo = (0, 25, 153)
screen.fill( azulfundo )
#caixas
screen_surface = pygame.Surface([450, 100])
screen_surface.fill((0,25,153)) 
screen.blit(screen_surface,(60,20))
image1 = pygame.image.load('images/imagea.svg') 
screen.blit(image1,(125, 0)) 

#bordas
borda_1 = pygame.draw.circle(screen, azulcirculo, (40,-30),500,30)
borda_2 = pygame.draw.circle(screen, azulcirculo, (40,-30),600,30)

#crédito
image2 = pygame.image.load('images/credit.png')
screen.blit(image2,(60,130))  
pygame.display.flip() 


#images
image3 = pygame.image.load('images/fs1urcbv.bmp')
image4 = pygame.image.load('images/d2v47czu.bmp')
image5 = pygame.image.load('images/9xkwbec5.bmp')
image6 = pygame.image.load('images/unknown.svg')
quizword = pygame.image.load('images/9ury7n0e.bmp')
image8 = pygame.image.load('images/2tgnfeqy.bmp')
errouB = pygame.image.load('images/j6hg7f08.bmp')
errouC = pygame.image.load('images/ggbbhntn.bmp')
errouA = pygame.image.load('images/zvp3qkce.bmp')
errouD = pygame.image.load('images/k3kgvdbh.bmp')
image10 = pygame.image.load('images/a5qvh3y1.bmp')

textA = pygame.image.load('images/776yuygt.bmp')
textB = pygame.image.load('images/ty7r6ybd.bmp')
textC = pygame.image.load('images/s7n2usr1.bmp')
textD = pygame.image.load('images/hbtviltr.bmp')
question2a = pygame.image.load('images/7l5gkrcd.bmp')
pontuacao = 0
question1a = pygame.image.load('images/dcjncg80.bmp')
question3 = pygame.image.load('images/drgqabgo.bmp')
question3a = pygame.image.load('images/t59n07ll.bmp')
question4 = pygame.image.load('images/aww4eyu1.bmp')
question4a = pygame.image.load('images/pbts0z83.bmp')
question5 = pygame.image.load('images/h89oga3n.bmp')
question5a = pygame.image.load('images/uk7ukzpi.bmp')
question6 = pygame.image.load('images/yleehx0i.bmp')
question6a = pygame.image.load('images/p1t9n4fl.bmp')
question7 = pygame.image.load('images/05nry4xm.bmp')
question7a = pygame.image.load('images/rbjhan2l.bmp')
question8 = pygame.image.load('images/jg8nljqb.bmp')
question8a = pygame.image.load('images/fr0r8uzu.bmp')
p2 = pygame.image.load('images/gz42bwy7.bmp')
p3 = pygame.image.load('images/5wckxncr.bmp')
p4 = pygame.image.load('images/9862zmqf.bmp')
p5 = pygame.image.load('images/y3fvqgek.bmp')
p6 = pygame.image.load('images/cs0pmxoo.bmp')
p7 = pygame.image.load('images/xksxotnm.bmp')
p8 = pygame.image.load('images/cwzw0q0l.bmp')
p0 = pygame.image.load('images/ifpsfqjs.bmp')
p1 = pygame.image.load('images/87cp8jek.bmp')
a = 120;
b = 2;

#1
pontuacao = 0
numero = 1
#images-----end
screen.blit(image3,(200,260))  
pygame.display.flip()
Not_Pressed = True
def Question_Prompt(certa, imagemQ, pergunta, custom, direita, altura):
    global pontuacao
    screen.fill( azulfundo )
    running = True
    #Quiz Images
    rectA = pygame.Rect((110,325), (150,101))
    rectB = pygame.Rect((325,325),(150,101))
    rectC = pygame.Rect((110,450), (150,101))
    rectD = pygame.Rect((325,450),(150,101))
    quizA = pygame.Surface([150,101])
    quizA.fill((0,25,153))
    quizB = pygame.Surface([150,101])
    quizB.fill((0,25,153))
    quizC = pygame.Surface([150,101])
    quizC.fill((0,25,153))
    quizD = pygame.Surface([150,101])
    quizD.fill((0,25,153))
    #Quiz Images Blit
    screen.blit(textB, (rectB.x, rectB.y))
    screen.blit(textA, (rectA.x, rectA.y))
    screen.blit(textC, (rectC.x, rectC.y))
    screen.blit(textD, (rectD.x, rectD.y))
    if custom == True:
        screen.blit(imagemQ,(direita,altura))  
    elif custom == False:
        screen.blit(imagemQ,(40,235))
    screen.blit(pergunta,(50,10))
    if certa == 'A':
        correct = rectA
    elif certa == 'B':
        correct = rectB
    elif certa == 'C':
        correct = rectC
    elif certa == 'D':
        correct = rectD
    pygame.display.flip()
    #Detectar click
    while running == True:
        mx, my = pygame.mouse.get_pos() 
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                running = False 
            if correct.collidepoint((mx, my)):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        screen.fill( azulfundo )
                        screen.blit(image10, (56,160))
                        pygame.display.flip()
                        pontuacao = pontuacao + 1
                        print(f'Certa voce esta com {pontuacao} ponto(s)!')
                        pygame.time.wait(6000)
                        running = False
                        
            elif rectA.collidepoint((mx,my)):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button ==1:
                        screen.fill( azulfundo )
                        if certa == 'B':
                            screen.blit(errouB, (56,160))
                            pygame.display.flip()
                        elif certa == 'C':
                            screen.blit(errouC,(56,160))
                            pygame.display.flip()
                        elif certa == 'D':
                            screen.blit(errouD, (56,160))
                            pygame.display.flip()
                        elif certa == 'A':   
                            screen.blit(errouA, (56,160))
                            pygame.display.flip()                        
                        pygame.time.wait(6000)
                        running = False
            elif rectB.collidepoint((mx,my)):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button ==1:
                        screen.fill( azulfundo )
                        if certa == 'B':
                            screen.blit(errouB, (56,160))
                            pygame.display.flip()
                        elif certa == 'C':
                            screen.blit(errouC,(56,160))
                            pygame.display.flip()
                        elif certa == 'D':
                            screen.blit(errouD, (56,160))
                            pygame.display.flip()
                        elif certa == 'A':
                            print("certa A")
                            screen.blit(errouA, (56,160))
                            pygame.display.flip()                     
                        pygame.time.wait(6000)
                        running = False
            elif rectC.collidepoint((mx,my)):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button ==1:
                        screen.fill( azulfundo )
                        if certa == 'B':
                            screen.blit(errouB, (56,160))
                            pygame.display.flip()
                        elif certa == 'C':
                            screen.blit(errouC,(56,160))
                            pygame.display.flip()
                        elif certa == 'D':
                            screen.blit(errouD, (56,160))
                            pygame.display.flip()
                        elif certa == 'A': 
                            print("certa A")
                            screen.blit(errouA, (56,160))
                            pygame.display.flip()                       
                        pygame.time.wait(6000)
                        running = False
            elif rectD.collidepoint((mx,my)):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button ==1:
                        screen.fill( azulfundo )
                        if certa == 'B':
                            screen.blit(errouB, (56,160))
                            pygame.display.flip()
                        elif certa == 'C':
                            screen.blit(errouC,(56,160))
                            pygame.display.flip()
                        elif certa == 'D':
                            screen.blit(errouD, (56,160))
                            pygame.display.flip()
                        elif certa == 'A':   
                            print("certa A")
                            screen.blit(errouA, (56,160)) 
                            pygame.display.flip()                      
                        pygame.time.wait(6000 )
                        running = False
pontuacao = 0
pygame.display.flip()
while Not_Pressed == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:

                print("It worked")
                Not_Pressed = False 
                screen.fill( azulfundo )
                music = ('images/yt1s.com-MusicKAHOOT-IT-Vylet-Trap-Remix_1.ogg')
                pygame.mixer.init()
                pygame.mixer.music.load(music)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.5)
                screen.blit(quizword, (215, 30))
                screen.blit(image8,(56,160))
                cube = pygame.Surface([250, 250])
                cube.fill((0,25,153))
                pygame.display.flip() 
                pygame.time.wait(6000)
                Question_Prompt('B',question1a, image8, False, 0,0)
                print("Passou 1")
                screen.fill( azulfundo )
                screen.blit(quizword, (215, 30))
                screen.blit(question2a, (56,160))
                pygame.display.flip()
                print("DisplayUpdated")
                quizabc = pygame.image.load('images/tlcyuigv.bmp')
                print("Esperando cooldown de 6 segundos")
                pygame.time.wait(6000)
                print("Cooldown passou")
                Question_Prompt('C',quizabc, question2a, False, 0,0)
                print("passou 2")
                screen.fill( azulfundo )
                screen.blit(quizword, (215, 30))
                screen.blit(question3, (56,160))
                pygame.display.flip()
                print("du")
                print("cooldown")
                pygame.time.wait(6000)
                print("passou")
                Question_Prompt('A', question3a, question3, True, 50,170)
                print("passou 3")
                screen.fill( azulfundo )
                screen.blit(quizword, (215, 30))
                screen.blit(question4, (56, 160))
                pygame.display.flip()
                print('du')
                print("cooldown")
                pygame.time.wait(6000)
                print("passou")
                Question_Prompt('D', question4a, question4, True, 50,150)
                print("Passou 4")
                screen.fill( azulfundo )
                screen.blit(quizword, (215,30))
                screen.blit(question5,(56,160))
                pygame.display.flip()
                print("du")
                print("cooldown")
                pygame.time.wait(6000)
                print("passou")
                Question_Prompt('A', question5a, question5, True, 50,150)
                print("Passou 5")
                screen.fill( azulfundo )
                screen.blit(quizword, (215,30))
                screen.blit(question6,(56,160))
                pygame.display.flip()
                print("du")
                print("Cooldown")
                pygame.time.wait(6000)
                print("passou")
                Question_Prompt('C', question6a, question6, True, 50,180)
                print("passou6")
                screen.fill( azulfundo )
                screen.blit(quizword, (215,30))
                screen.blit(question7,(56,160))
                pygame.display.flip()
                print("du")
                print("Cooldown")
                pygame.time.wait(6000)
                print("passou")
                Question_Prompt('C', question7a, question7, True, 50,150)
                print("passou 7")
                screen.fill( azulfundo )
                screen.blit(quizword, (215,30))
                screen.blit(question8,(56,160))
                pygame.display.flip()
                print("du")
                print("Cooldown")
                pygame.time.wait(6000)
                print("passou") 
                Question_Prompt('A', question8a, question8, True, 50,150)
                screen.fill( azulfundo )
                if pontuacao == 0:
                    screen.blit(p0,(56,160))
                    print("Voce foi mal! Voce esta com 0 pontos no total")
                elif pontuacao == 1:
                    print("Falta mais estudo! Voce tirou 1")
                    screen.blit(p1,(56,160))
                elif pontuacao == 2:
                    print("Quase-La voce tirou 2")
                    screen.blit(p2,(56,160))
                elif pontuacao == 3:
                    print("Voce tirou 3... mais umas horas de estudo e voce chega lá!")
                    screen.blit(p3,(56,160))
                elif pontuacao == 4:
                    print("Voce tirou 4, isto e 50%, quase a media! Voce consegue!")
                    screen.blit(p4,(56,160))
                elif pontuacao == 5:
                    print("Voce tirou mais de 60%, parabens! Mas, acho que voce consegue mais!")
                    screen.blit(p5,(56,160))
                elif pontuacao == 6:
                    print("Voce tirou 7, isto equivale mais de 75%, parabens!!")
                    screen.blit(p6,(56,160))
                elif pontuacao == 7:
                    print("Voce e um deus, conseguiu 7 quase total!")
                    screen.blit(p7,(56,160))
                elif pontuacao == 8:
                    print("Wow, estou surpreendido, voce conseguiu a nota máxima! Parabéns!")
                    screen.blit(p8,(56,160))
                pygame.display.flip()
                pygame.time.wait(6000)
                pygame.QUIT()
            elif numero%2:
                print("1 alternativa")
                screen.blit(image5,(200,160))
                pygame.display.flip()    
                numero = numero + 1
            else:
                print("2 Alternativa")
                screen.blit(image4,(200,160))
                pygame.display.flip()
                numero = numero + 1



    


#main loop
Teste = True
while Teste:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
