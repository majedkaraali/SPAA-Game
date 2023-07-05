import random 
import pygame
pygame.init()
WIDTH=1280
HEIGHT=677
score=0
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hunt")

class Bullet:
    width = 3
    height = 7
    vel_y = -10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_bullet(self):
        self.y += self.vel_y

    def draw_bullet(self):
        pygame.draw.rect(win, ('black'), (self.x, self.y, self.width, self.height))


class Player:
    x=350
    y=566
    width=50
    height=50
    player_alive=True
    vel_x = 0
    vel_y = 0
    move_speed = 6
    bullets = []
    shoot_delay = 100  
    last_shot_time = 0

    def move_player(self):
        if keys[pygame.K_LEFT]:
            vel_x = -self.move_speed
        elif keys[pygame.K_RIGHT]:
            vel_x = self.move_speed
        else:
            vel_x = 0

        self.x += vel_x
        self.x = max(0, min(self.x, WIDTH - self.width))
        
    def update_player(self):
        pl = pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def can_shoot(self):
        current_time = pygame.time.get_ticks()
        return current_time - self.last_shot_time >= self.shoot_delay

    def shoot(self):
        if self.can_shoot():
            bullet = Bullet(self.x + self.width // 2 - Bullet.width // 2, self.y)
            self.bullets.append(bullet)
            self.last_shot_time = pygame.time.get_ticks()

    def move_bullets(self):
        for bullet in self.bullets:
            bullet.move_bullet()

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.draw_bullet()



class Enemy:
    def __init__(self,x,y,width,height,vel,move_dir):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=vel
        self.move_dir=move_dir

    def set_x(self,x):
        self.x=x
    def move_enemy(self):
        

        if self.move_dir=='right':
            if self.x<WIDTH-60:
                self.x+=self.vel
            else:
                enemy_lsit.remove(enemy)

        elif self.move_dir=="left":
            if self.x>60:
                self.x+=self.vel
            else:
                enemy_lsit.remove(enemy)


    def update_enemy(self):
        en = pygame.draw.rect(win, (29, 84, 158), (self.x, self.y, self.width, self.height))



p1=Player()

enemy_lsit=[]
clock = pygame.time.Clock()
pygame.font.init()
pygame.mixer.init()




def generate_enemies():
    if len(enemy_lsit)<2:
        move_dircton=random.randint(0,1)
        if move_dircton==1:
            vel=2
            x=random.randint(-350,-50)
            mdir='right'
        else:
            vel=-2
            x=random.randint(WIDTH+50,WIDTH+350)
            mdir='left'
        
        enemy=Enemy(x,10,50,50,vel,mdir)
        enemy_lsit.append(enemy)
    else:
        print("A")

   



run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    clock.tick(60)
    win.fill('aqua')

    p1.move_player()
    p1.update_player()
    p1.move_bullets() 
    p1.update_bullets() 
    generate_enemies()


    if keys[pygame.K_SPACE]:
        p1.shoot()
    for enemy in enemy_lsit:
        enemy.move_enemy()
        enemy.update_enemy()
        

    pygame.display.update()

    

pygame.quit()