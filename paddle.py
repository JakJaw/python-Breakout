import pygame
WHITE = (255, 255, 255)


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveLeft(self, distance):
        self.rect.x -= distance
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, distance):
        self.rect.x += distance
        if self.rect.x > 700:
            self.rect.x = 700