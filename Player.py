import pygame

class Player:

    def __init__(self, posX, poY):
        self.world_position = (posX, poY)
        self.img = pygame.image.load("Emoji.png")

    def move(self, pos):
        self.world_position = pos

    def draw(self, screen):
        if self.world_position[1] % 2 == 0:
            screen.blit(self.img, (self.world_position[0]*48, self.world_position[1]*40))
        else:
            screen.blit(self.img, (self.world_position[0] * 48 + 24, self.world_position[1] * 40))
