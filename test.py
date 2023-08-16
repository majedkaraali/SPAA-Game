import pygame

class Sprite():
    def __init__(self, x, y, frame_width, frame_height):
        self.spritesheet = pygame.image.load("src/img/HMV.png")
        self.sprite_width=self.spritesheet.get_width()
        self.sprite_height= self.spritesheet.get_height()
        self.width=frame_width
        self.height=frame_height
        self.x=x
        self.y=y
        self.frames = []  
        self.current_frame = 0
        
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        
        self.load_frames(self.spritesheet, 0, 0, self.sprite_width, self.sprite_height, frame_width, frame_height)
    
    def load_frames(self, spritesheet, x, y, width, height, frame_width, frame_height):
        self.image.blit(spritesheet, (0, 0), (x, y, width, height))
        
        for y_offset in range(0, height, frame_height):
            for x_offset in range(0, width, frame_width):
                frame_rect = pygame.Rect(x_offset, y_offset, frame_width, frame_height)
                frame = self.image.subsurface(frame_rect)
                self.frames.append(frame)

    def draw(self,screen):
        screen.blit(sprite.frames[sprite.current_frame], (self.x, self.y))
        sprite.current_frame += 1
        if sprite.current_frame >= len(sprite.frames):
            sprite.current_frame = 0  


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Example")




sprite = Sprite( 20,20, 88, 66)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  
    
    sprite.draw(screen)
    
    pygame.display.update()

pygame.quit()
