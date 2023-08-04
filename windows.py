import pygame
from GUI import Button
pygame.init()
width,height=1100,660
gui=pygame.image.load('src/img/GUI/background.png').convert_alpha()
font = pygame.font.Font(None, 24)

def pause_screen(screen,state):
    pygame.draw.rect(state.rewards_surface,state.border_color, state.frame_surface.get_rect(), state.border_width)
    screen.blit(state.frame_surface, state.frame_position)


    resume_button = pygame.draw.rect(state.frame_surface, (0, 0, 255),state.resume_button_rect)
    resume_button_text = font.render("Resume", True, (255, 255, 255))
    resume_button_text_rect = resume_button_text.get_rect(center=resume_button.center)
           

    mainmenu_button=pygame.draw.rect(state.frame_surface,(0, 0, 255),state.main_menu_button_rect)
    mainmenu_button_text=font.render("Main menu", True, (255, 255, 255))
    mainmenu_button_text_rect=mainmenu_button_text.get_rect(center=mainmenu_button.center)

    exit_button=pygame.draw.rect(state.frame_surface,(0, 0, 255),state.exit_button_rect)
    exit_button_text=font.render("Exit", True, (255, 255, 255))
    exit_button_text_rect=exit_button_text.get_rect(center=exit_button.center)


    state.frame_surface.blit(resume_button_text,resume_button_text_rect)
    state.frame_surface.blit(mainmenu_button_text,mainmenu_button_text_rect)
    state.frame_surface.blit(exit_button_text,exit_button_text_rect)



def reward_screen_view(screen,state):
        pygame.draw.rect(state.rewards_surface,state.border_color, state.rewards_surface.get_rect(), state.border_width)
        screen.blit(state.rewards_surface, state.reward_scr_position)
        state.rewards_surface.fill('silver')


        
        main_menu_text = font.render("Main Menu", True, (255, 255, 255))
        main_menu_text_rect=main_menu_text.get_rect(center=state.main_menu_btn_rect.center)

        
        exit_text = font.render("Exit ", True, (255, 255, 255))
        exit_text_rect=exit_text.get_rect(center=state.exit_btn_rect.center)


        scor_text= font.render("Score: 0", True, (255, 255, 255))
        score_pos=((state.rwd_surface_width//2)-scor_text.get_width()//2,80)

        high_score= font.render("High Score: 0", True, (255, 255, 255))
        high_score_pos=((state.rwd_surface_width//2)-high_score.get_width()//2,120)


        died_text= font.render(" YOU HAVE BEEN DESTROYED ! ", True, (255, 255, 255))
        died_text_pos=((state.rwd_surface_width//2)-(died_text.get_width()//2),20)


        state.rewards_surface.blit(main_menu_text,main_menu_text_rect)
        state.rewards_surface.blit(exit_text,exit_text_rect)
        state.rewards_surface.blit(died_text,died_text_pos)
        state.rewards_surface.blit(scor_text,score_pos)
        state.rewards_surface.blit(high_score,high_score_pos)




class Main_menu_window():

    def __init__(self):
        self.buttons=[]
        self.image=pygame.image.load('src/img/GUI/background.png').convert_alpha()
        self.play_button=Button(width//2,180,"Play")
        self.options_button=Button(width//2,260,"Options")
        self.Credits_button=Button(width//2,340,"Credits")
        self.Exit_button=Button(width//2,420,"Exit")
        self.buttons.extend([self.play_button, self.options_button, self.Credits_button,self.Exit_button])

    def draw(self,screen):
      screen.blit(self.image, (0,0))
      for button in self.buttons:
          button.place(screen)
    
    def get_buttons(self):
        return self.buttons
    
  
 
    


