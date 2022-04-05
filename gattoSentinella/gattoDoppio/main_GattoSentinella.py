
#-------------------------Run this to test the agents----------------------------------------------#
import pygame
import time

from Agent_GattoSentinella import Agent
from Environment_GattoSentinella import Env, Matrix 

#colours
ORANGE = (255, 165, 0)
GREEN = (0, 150, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLACK = (0,0,0)

def show_info(cheese, mouse):
    pygame.draw.rect(gameDisplay, BLACK, [0, 800, 800, 5])
    font = pygame.font.SysFont(None, 40)
    text1 = font.render("Total Cheese Eaten: "+str(cheese), True, GREEN)
    text2 = font.render("Total Mouse Caught: "+str(mouse), True, RED)
    
    gameDisplay.blit(text1,(50,810))
    gameDisplay.blit(text2,(50,855))	

def draw_rect(color, x, y, width, height):
    pygame.draw.rect(gameDisplay, color, [x*width, y*height, width, height], 10)
    pygame.display.update()
    time.sleep(0)

#-------------------------------------------------------------------------------------------------------------------------------------------------#
# Pygame
display_width, display_height = 800, 900
pygame.init()
pygame.display.set_caption('Tom & Jerry AI Agents')
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

# env, grid e agent definition
pct_obstacles = 0.04
cat2_mode = 'misto'
map = Matrix(rows=10, columns=10, max_pct_obstacles=pct_obstacles, cat2_mode=cat2_mode)
env = Env(gameDisplay, map, cat2_mode)
mouse = Agent(env, possibleActions=4)
# Epochs
num_episodes = 10000

# Load the policy
if cat2_mode == 'verticale':
    dir = 'policies/gattoSentinella/gattoDoppio/verticale/'
else:
    dir = 'policies/gattoSentinella/gattoDoppio/misto/'

mouse.load_policy(dir+'mouse.pickle')

# Stats
total_mouse_caught = 0
total_cheese_eaten = 0
total_toccatemuro = 0
total_roccateostacolo = 0

for i_episode in range(1, num_episodes+1):
    env.set_obstacles(env.load_obstacles(map.OBSTACLES,pct_obstacles)) # Load different obstacles at each epoch
    state = env.reset()
    action_mouse = mouse.take_action(state['mouse'])
    
    # Gatto sentinella doppio
    cat1_direction = 2
    if cat2_mode == 'verticale':
        cat2_direction = 2
    elif cat2_mode == 'misto':
        cat2_direction = 0

    # Render the environment        
    env.render(i_episode)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   #close the window
                quit() 

        next_state, reward, done, info, cat1_direction, cat2_direction, toccate_muro, toccate_ostacolo = env.step(action_mouse, cat1_direction, cat2_direction)

        total_toccatemuro += toccate_muro
        total_roccateostacolo += toccate_ostacolo

        # Render the environment
        gameDisplay.fill(WHITE)         
        env.render(i_episode)
        show_info(total_cheese_eaten, total_mouse_caught)

        # Updating the display
        pygame.display.update()
        clock.tick(9999999999999999999999999999)
        
        if done:
            if info['cheese_eaten']:
                total_cheese_eaten += 1
                draw_rect(GREEN, info['x'], info['y'], info['width'], info['height'])       
            
            if info['mouse_caught']:
                total_mouse_caught += 1
                draw_rect(RED, info['x'], info['y'], info['width'], info['height'])    
            # Episode termination   
            break
       
        # Update state and action
        state = next_state
        action_mouse = mouse.take_action(state['mouse'])
        

print('muro: ', total_toccatemuro)
print('ostacolo: ', total_roccateostacolo)
print('topo: ', total_cheese_eaten)
print('gatto: ', total_mouse_caught)
time.sleep(2)
pygame.quit()