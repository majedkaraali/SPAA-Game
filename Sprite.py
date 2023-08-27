import pygame
import os

class Sprite:
    def __init__(self, spritesheet_path, width, height, frame_width, frame_height, draw_limit=-1):
        self.spritesheet = pygame.image.load(spritesheet_path)
        self.width = width
        self.height = height
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.draw_limit = draw_limit
        self.draw_count = 0
        self.current_frame = 0
        self.image = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

    def update(self):
        self.current_frame += 1
        if self.current_frame * self.frame_width >= self.spritesheet.get_width():
            self.current_frame = 0
            self.draw_count += 1

            if self.draw_limit != -1 and self.draw_count >= self.draw_limit:
                self.draw_count = 0

        self.image = self.spritesheet.subsurface(
            pygame.Rect(
                self.current_frame * self.frame_width,
                0,
                self.frame_width,
                self.frame_height
            )
        )

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))
