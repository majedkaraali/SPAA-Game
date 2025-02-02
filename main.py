"""
This is the main file which is the start point of the game 
Required libares are (pygame,math,random)

Author : Majed Karaali

"""



import pygame

# Setting default values

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
pygame.mixer.set_num_channels(64)


screen_width = 1100
screen_height = 660

icon = pygame.image.load('icon.png')  
icon = pygame.transform.scale(icon, (32, 32))  
pygame.display.set_icon(icon) 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Aero Assault")


intro_image = pygame.image.load("src/img/meta/intro_image.png").convert_alpha()
intro_rect = intro_image.get_rect()
background_color=('black')

intro_duration = 5000  
intro_running=True
intro_complete=False
intro_timer = 0
alpha = 255  




# Intro loop

while intro_running:
    screen.fill(background_color)  
    clock.tick(60)

    events = pygame.event.get()
        
        
    for event in events:
            if event.type == pygame.QUIT:
                intro_running = False

    if intro_timer < intro_duration:
            screen.blit(intro_image, intro_rect)
            alpha -= 1
            intro_image.set_alpha(alpha)
            pygame.display.update()
            intro_timer += clock.get_time()
            pygame.display.flip()

    else:
        intro_running=False
        intro_complete=True
          

if  intro_complete:
    # Importing models,models and states
    from states import states
    from objects.objects import *
    from windows import *
    from states.survival_state import *
   

    # Setting state to MENU STATE
    state=states.state
    state.menu_state()
    


    #  Game main loop Start
    while state.running:
        current_state=state
        clock.tick(60)
        events = pygame.event.get()
        
        
        for event in events:
            if event.type == pygame.QUIT:
                state.running = False

        
        current_state.handle_events(events)
        current_state.draw(screen)

        #  print(clock.get_fps())       Uncomment this if you want to debug FPS
        pygame.display.flip()

    pygame.quit()



