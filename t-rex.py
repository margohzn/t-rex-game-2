import pygame
from pygame.locals import *
import random 

pygame.init()

#screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((173,216,230))

#additional
pygame.display.set_caption("T-rex game!")
FONT = pygame.font.SysFont("Times new roman", 50)


#variables for the game 
ground_scroll = 0 
scroll_speed = 5
score = 0 
moving = False
game_over = False
score = 0 
tree_gap = 200 
tree_frequency = 1500 #in millieseconds, time till a new tree is generated in the game diffrent to the gap 
jumped_tree = False
last_tree = pygame.time.get_ticks() - tree_frequency


# loading images for the ground (what will scroll while moving = True)
bg = pygame.image.load("ground.png")
clouds = pygame.image.load("cloud.png")


class Trex(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1, 4):
            timg = pygame.image.load(f"trex{i}.png").convert_alpha()
            self.images.append(timg)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False
        self.jumping = False

    def update(self, game_over, moving, screen_height):
        self.counter += 1 
        if not game_over:
            if moving:
                self.vel += 1
                if self.vel > 10:
                    self.vel = 10
                self.rect.y += self.vel
                if self.rect.bottom >= screen_height - 50:
                    self.rect.bottom = screen_height - 50
                    self.jumping = False
                    self.vel = 0

            keys = pygame.key.get_pressed()
            if keys[K_SPACE] and not self.jumping:
                self.jumping = True
                self.vel = -15  

            self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.image, self.vel * -2)
        else:
            self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.image, -90)



