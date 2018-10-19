import pygame
from pygame.sprite import Sprite


class BadBullets(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(BadBullets, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bulletWidth +4, ai_settings.bulletHeight +1)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_settings.bulletColor
        self.speedFactor = ai_settings.bulletSpeed

    def update(self):
        self.y += self.speedFactor *.8
        self.rect.y = self.y

    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

