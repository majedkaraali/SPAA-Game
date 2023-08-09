from states import GameState
import objects,os
import pygame 
from windows import game_windows
from enemy_generator import Generate_enemies



background=pygame.image.load('src/img/backgrounds/background1.png').convert_alpha()
statics_image=pygame.image.load('src/img/backgrounds/statics.png').convert_alpha()

font_path = os.path.join("src/fonts", "OCRAEXT.ttf")
font_size = 19 
font = pygame.font.Font(font_path, font_size)


        



width,height=(1100,660)

windo=game_windows()


class Level_Play(GameState):

 
    

    def __init__(self,state,level,test):

      #  super().__init__()
        self.score=0
       # print("GG")
        self.running=True
        self.force_reload=False
        self.level=level
        self.wave=0
        self.complete=False
        self.game_over=False
        self.close=False
        self.state=state
        self.buttons=windo.get_buttons()
        self.mouse_button_pressed=False
        self.paues=False
        self.reward_screen=False
        self.enemy_list=[]
        self.test=test
        self.player=objects.Player(400,height-107,'Unnamed')
        self.enemies=Generate_enemies(self.player)
        
    def handle_events(self, events):
     #   print(self.test)
        tab_pressed = False
        for event in events:

            if event.type == pygame.QUIT:
                self.running = False
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_pressed=True

                if self.paues:
                    if windo.main_menu_button.holding:
                  #      self.enemy_list.clear()
                        self.state.menu_state()

                    if windo.resume_button.holding:
                        self.paues=False

                if self.complete:
                    self.level.unluck_level(int(self.level.get_number())+1)
                    if windo.main_menu_button.holding:

                        self.state.menu_state()

                    if windo.next_level.holding:
                        next_level=self.level.next_level()
                        self.state.level_state(next_level)

            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_pressed = False
            

            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    if  not self.complete and not self.paues:
                        self.paues = True

                    elif self.paues:
                        self.paues=False
                    

                
                if event.key == pygame.K_TAB and not tab_pressed:
                    if not self.player.forced:
                        self.player.next_lock()
                        tab_pressed = True
                        
                if event.key == pygame.K_r:
                    self.player.reload_start_time=pygame.time.get_ticks()
                    self.player.droped_ammo+=self.player.magazine
                    self.player.magazine=0

 
            elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_TAB:
                        tab_pressed = False

        if self.mouse_button_pressed:
            if not self.player.forced:
                if not self.paues:
                    self.player.shoot()


    
    
    def generate_enemies(self,wave):
        self.enemy_list=self.enemies.respawn_wave(wave)
           

    def get_enemies(self):
        return self.enemy_list
        
    def statics(self,screen):
        statics_rect=statics_image.get_rect()
        statics_rect.topleft=(0,630)

        screen.blit(statics_image,statics_rect)

        if self.player.reloading:
            magazine='---'
        else:
            magazine=str(self.player.magazine)
        bullets=str(self.player.ammo)

        if self.player.reloading_pods:
            missiles='--'
        else:
            missiles=self.player.ready_to_fire_missiles

        storage=self.player.missiles_storage
        bullets_text = font.render(f"bullets: {magazine}/{bullets}", True, 'black')
        bullets_text_pos=(width-375,height-25)
        missiles_text = font.render(f"missiles: {missiles}/{storage}", True, 'black')
        missiles_text_pos=(width-550,height-25)
        heath_value=self.player.health
        heatl_text = font.render(f"health: {str(heath_value)}", True, 'black')
        heatl_text_pos=(width-170,height-25)
      
        screen.blit(bullets_text, bullets_text_pos)
        screen.blit(missiles_text, missiles_text_pos)
        screen.blit(heatl_text, heatl_text_pos)



    def draw(self,screen):
      #  print(self.enemy_list)
        screen.blit(background,background.get_rect())
        if not (self.paues) :
            if not self.game_over:
                if not self.complete:
                    self.statics(screen)

                    #HANDLE self.PLAYER
                    if not self.player.forced:
                        
                        self.player.move_player()
                        if len(self.enemy_list)==0:
                            
                            self.wave+=1
                            if self.wave<=self.level.get_waves_number():
                    
                                self.generate_enemies(self.level.make_wave(self.wave))
                                
                            else:
                                self.complete=True
                                
                            print(self.enemy_list)


                    self.player.update_bullets(screen)
                    self.player.update_player(screen)
                    self.player.move_bullets() 
                    self.player.move_missiles()
                    self.player.update_missiles(screen)
                    self.player.chek_magazine()
                    self.player.chek_missile_lounchers_pods()
                    self.player.move_drops(screen,self.player)
                    self.player.is_destroyed()   
                    self.player.get_enemies=self.get_enemies() 
                    
                    
                    
                    #CLEAN BULLETS KEYS
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        if not self.player.forced:
                            self.player.shoot()
                    elif keys[pygame.K_f]:
                        if not self.player.forced:
                            self.player.fire_missile(self.player)
                        
                    enemies_to_remove = []
                    bullets_to_remove = []
                    missiles_to_remove=[]



                    # HANDLE ENEMIES
                    for enemy in self.enemy_list:
                        enemy.move_enemy(screen)
                        enemy.update_enemy(screen)
                        if enemy.destroyed:
                            enemies_to_remove.append(enemy)
                        if enemy.check_kill(self.player.bullets):
                            self.score+=100
                            drop=objects.Item(enemy.get_centerx(),enemy.y,'gift')
                            self.player.drops.append(drop)
                            enemies_to_remove.append(enemy)

                        if enemy.move_dir=='left':
                            if (enemy.x)<5:
                                enemy.move_dir='right'
                                enemy.recharge()
                        elif enemy.move_dir=='right':
                            if (enemy.x)>width-5-enemy.get_width():
                                enemy.move_dir='left'
                                enemy.recharge()

                        if enemy.y>580:
                            enemy.destroyed=True
                            enemies_to_remove.append(enemy)




                
                    # HANDLE BULLETS
                    for bullet in self.player.bullets:
                        if bullet.out_of_range():
                            bullets_to_remove.append(bullet)
            
                        elif bullet.hitted:
                            self.score+=20
                            bullets_to_remove.append(bullet)



                    # HANDLE MISSILES
                    for missile in  self.player.missiles:
                        if missile.y<=-10:
                            missiles_to_remove.append(missile)
                        elif missile.hit_target():
                            self.score+=200
                            missiles_to_remove.append(missile)
                            enemies_to_remove.append(missile.target)
                            
                    # CLEAN ENEMEIS
                    if len(enemies_to_remove)>0:
                        for enemy in enemies_to_remove:
                            enemy.destroyed=True
                            if enemy in self.enemy_list:
                                self.enemy_list.remove(enemy)


                    #CLEAN BULLETS
                    for bullet in bullets_to_remove:
                        self.player.bullets.remove(bullet)

                    #CLEAN MISSILES
                    for missile in missiles_to_remove:
                        self.player.missiles.remove(missile)

                    #ATTACK self.PLAYER
                    for enemy in self.enemy_list:
                        enemy.attack(self.player)
                        enemy.move_bombs()
                        enemy.draw_bombs(screen)
                        break
                                

                    if self.player.destroyed:
                        self.game_over=True

                elif self.complete:
                    windo.reward_window()
                    windo.draw(screen)
                    windo.draw_frames(screen)                   


            elif (self.reward_screen):
                windo.reward_window()
                windo.draw(screen)
                windo.draw_frames(screen)
  

        elif (self.paues):
            windo.puse_window()
            windo.draw(screen)
            windo.draw_frames(screen)
  
        
            
            