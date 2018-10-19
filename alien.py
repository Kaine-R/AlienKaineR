import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.a1Image = [pygame.image.load('images/alien1_0.png'), pygame.image.load('images/alien1_1.png')]
        self.a2Image = [pygame.image.load("images/alien2_0.png"), pygame.image.load("images/alien2_1.png")]
        self.a3Image = [pygame.image.load("images/alien3_0.png"), pygame.image.load("images/alien3_1.png")]
        self.expo = [pygame.image.load("images/bomb1.png"), pygame.image.load("images/bomb2.png"), pygame.image.load("images/bomb3.png"), pygame.image.load("images/bomb4.png")]
        self.rect = self.a1Image[0].get_rect()

        self.direction = 1
        self.type = 0
        self.deathnum = 0
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.ai_settings.alienSpeed * self.ai_settings.alienDirection * self.ai_settings.gameSpeed
        self.rect.x = self.x
        if self.type == 3:
            self.ufoRect.x += self.ai_settings.alienSpeed*1.5

    def checkEdges(self):
        screenRect = self.screen.get_rect()
        if self.rect.x >= screenRect.right - 50 or self.rect.x <= screenRect.left and self.type != 3:
            return True

    def blitAliens(self, settings):
        if self.type == 0:
            if settings.timer < settings.frameChange:
                self.screen.blit(self.a1Image[0], self.rect)
            else:
                self.screen.blit(self.a1Image[1], self.rect)
        elif self.type == 1:
            if settings.timer < settings.frameChange:
                self.screen.blit(self.a2Image[0], self.rect)
            else:
                self.screen.blit(self.a2Image[1], self.rect)
        elif self.type == 2:
            if settings.timer < settings.frameChange:
                self.screen.blit(self.a3Image[0], self.rect)
            else:
                self.screen.blit(self.a3Image[1], self.rect)
        elif self.type == 3:
                self.screen.blit(self.UFOimage, self.ufoRect)
        else:
            self.death()

        if settings.timer > settings.frameChange*2:
            settings.timer = 0

        settings.timer += 1


    def ufo(self):
        self.UFOimage = pygame.image.load("images/ufo.png")
        self.type = 3
        self.ufoRect = self.UFOimage.get_rect()
        self.ufoRect.x, self.ufoRect.y = -30, 40


    def updateUfo(self):
        self.ufoRect.x += self.ai_settings.alienSpeed *2

    def drawUfo(self):
        self.screen.blit(self.image, self.ufoRect)

    def death(self): #aliens):
        if self.deathnum <= 20:
            self.image = self.expo[0]

        elif self.deathnum <= 30:
            self.image = self.expo[1]
        elif self.deathnum <= 50:
            self.image = self.expo[2]
        elif self.deathnum <= 60:
            self.image = self.expo[3]
        else:
            self.kill()
        self.deathnum += 1
        self.screen.blit(self.image, self.rect)

        #aliens.remove(self)