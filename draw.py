import pygame
from solve import solve
black = [0, 0, 0]
yellow=[248,230,33]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue=[0,0,255]

width=400
height=500
pygame.init()

pygame.display.set_caption("robot")

pygame.font.init()
surface = pygame.display.set_mode((400,500))
pygame.display.flip()

solve=solve()
solve.solve()
solution=solve.solution



def write_action(action,num):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(num)+" "+action, True, white, black)
    textRect = text.get_rect()
    textRect.center = (200, 450)
    pygame.draw.rect(surface, white, pygame.Rect(0, 400, 400, 100))

    return text,textRect
def seed(action,x,y):
    if action=="seed":
        if x=="left":
            xpos=100
        elif x=="right":
            xpos=300
        if y=="up":
            ypos=100
        elif y=="down":
            ypos=300
        pygame.draw.circle(surface, black,(xpos,ypos),20)


def draw_square(action,x,y,explored):
    color=yellow
    if action != "seed":
        if x=="left":
            xpos=0
        elif x== "right":
            xpos=200
        if y=="up":
            ypos=0
        elif y=="down":
            ypos=200
        if (x,y) in explored:
            print("hi")
            color=red
            pygame.draw.rect(surface, color, pygame.Rect(xpos, ypos, 200, 200))
            seed("seed",x,y)
        else:
            pygame.draw.rect(surface, color, pygame.Rect(xpos, ypos, 200, 200))
explored=[]
runinng= True
while runinng:
    surface.fill(white)
    draw_square("any",solve.initial[0],solve.initial[1],[])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        for i in range(len(solution[1])):
                state=solution[1][i]
                action=solution[0][i]
                draw_square(action,state[0],state[1],explored)
                seed(action,state[0],state[1])
                text, textRect = write_action(action,i)
                surface.blit(text, textRect)
                explored.append((state[0],state[1]))
                pygame.display.update()
                pygame.time.wait(2000)
        solve.print()
        pygame.quit()


