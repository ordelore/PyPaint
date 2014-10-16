import pygame, sys

##TOP LEVEL CONSTANTS

WINDOWWIDTH = 320

WINDOWHEIGHT = 240

GAMETITLE = "Paint"

#WHITE=[255,255,255]; RED=[255,0,0]; GREEN=[0,255,0]

#BLUE=[0,0,255]; BLACK=[0,0,0];

size = [320,240]

color = [0,0,255]

def main():

#set up display

pygame.init()

DISPLAY=pygame.display.set_mode(size)

pygame.display.set_caption(GAMETITLE)

DISPLAY.fill(BLACK)

pygame.display.update()

#draw rectangle code: pygame.draw.rect(DISPLAY,color,x,y,width,height)

pygame.draw.rect(DISPLAY,RED,(0,0,30,48))

pygame.draw.rect(DISPLAY,GREEN,(0,48,30,48))

pygame.draw.rect(DISPLAY,BLUE,(0,96,30,48))

pygame.draw.rect(DISPLAY,WHITE,(0,144,30,48))

pygame.display.update()

while True:

for event in pygame.event.get():

if event.type == pygame.QUIT:

pygame.quit(); sys.exit();

if event.type == pygame.MOUSEBUTTONDOWN:

(x, y) = pygame.mouse.get_pos()

if (0 < x < 30) and (0 < y < 48):

#RED

color = [255,0,0]

elif (0 < x < 30) and (48 < y < 96):

#GREEN

color = [0,255,0]

elif (0 < x < 30) and (96 < y < 144):

#BLUE

color = [0,0,255]

elif (0 < x < 30) and (144 < y < 192):

#WHITE

color = [255,255,255]

else:

pygame.draw.circle(DISPLAY, color, (x,y), 2, 0)

pygame.display.update()

main()
