import pygame
import random

pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("YEAH YEAH YEAH, THIS IS WAR")
clock = pygame.time.Clock()


doexit = False
class card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    def draw(self,x,y):
        pygame.draw.rect(screen,(255,255,255), (x,y,100,180))
        pygame.draw.rect(screen,(0,0,0), (x,y,100,180),3)
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render(str(self.number),1,(0,0,0))
        text2 = font.render(str(self.suit),1,(250,0,0))
        screen.blit(text,(x+30,y+30))
        screen.blit(text2,(x+10,y+60))

       
#jack is 11, queen is 12, king is 13
Deck = list()
for j in range(4):
    for i in range(13):
        Deck.append(card(j,i))
random.shuffle(Deck)
#break cards into player's hands
p1hand=list()
p2hand=list()
p1Discard=list()
p2Discard=list()

for i in range(26):
    p1hand.append(Deck[i])
for j in range(26,52):    #28-52
    p2hand.append(Deck[j])
  
turn = False

while not doexit:
#gameloop---------------------------------------------------------------------------------
  clock.tick(60)
  event = pygame.event.wait() 
  #I/O section----------------------------------------------------------------------------
  #for event in pygame.event.get():
  if event.type == pygame.QUIT:
          doexit = True
  if event.type == pygame.MOUSEBUTTONDOWN:
      turn = True
  if event.type == pygame.MOUSEBUTTONUP:
      turn = False
  if event.type == pygame.MOUSEMOTION:
      mousePos = event.pos
  #game logic-----------------------------------------------------------------------------
  if len(p1hand)<=0 or len(p2hand)<=0:
      if len(p1Discard)>len(p2Discard):
          print("player 1 wins!")
      else:
          print("player 2 is victorious")
      doExit = True    
    
  if turn and len(p1hand)>0 and len(p2hand)>0:
      if p1hand[len(p1hand)-1].number>p2hand[len(p2hand)-1].number:
          print("player one wins round!")
          p1Discard.append(p1hand[len(p1hand)-1])
          p1Discard.append(p2hand[len(p2hand)-1])
          p1hand.pop(len(p1hand)-1)
          p2hand.pop(len(p2hand)-1)
      else:
          print("player 2 wins this one.")
          p2Discard.append(p1hand[len(p1hand)-1])
          p2Discard.append(p2hand[len(p2hand)-1])
          p1hand.pop(len(p1hand)-1)
          p2hand.pop(len(p2hand)-1)





    

#render section-------------------------------------------------------------------------
  screen.fill((0,150,0))

#print the whole deck
  #for i in range(52):
   #   Deck[i].draw(20+i*5, 20+i*3)

  for i in range(0,len(p1hand)):
      p1hand[i].draw(200,50)
  for i in range(0,len(p2hand)):
      p2hand[i].draw(200,250) 
    #draw dicard pile
  for i in range(0,len(p1Discard)):
      p1Discard[i].draw(400+4*i,50)
  for i in range(0,len(p2Discard)):
      p2Discard[i].draw(400+4*i,250)      
    
  print("p1hand size:", len(p1hand))
  print("p2hand size:", len(p2hand))  
  print("p1 discard size:", len(p1Discard))
  print("p2 discard size:", len(p2Discard))


  pygame.display.flip()

#end game loop---------------------------------------------------------------------------
pygame.quit()
