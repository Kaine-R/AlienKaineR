import random
import pygame
from pygame.sprite import Sprite


class Background(Sprite):
    def __init__(self, ai_settings, screen):
        super(Background, self).__init__()
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.ai_settings = ai_settings

        self.rectSize = random.randint(1, 6)
        self.rect = pygame.Rect(random.randint(0, int(self.screenRect.right)), -10, self.rectSize, self.rectSize)
        self.speed = 1.25

        self.y = float(self.rect.y)
        self.rect.x = random.randint(0, int(self.screenRect.right))

    def update(self):
        self.y += self.speed * self.ai_settings.gameSpeed
        self.rect.y = self.y

    def createStar(self):
        pygame.draw.rect(self.screen, (122, 100, 100), self.rect)
