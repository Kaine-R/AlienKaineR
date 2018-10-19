import pygame

class Ship:

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.normalImage = pygame.image.load('images/ship.png')
        self.expo = [pygame.image.load("images/bomb1.png"), pygame.image.load("images/bomb2.png"), pygame.image.load("images/bomb3.png"), pygame.image.load("images/bomb4.png")]
        self.image = self.normalImage
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.type = 0
        self.deathnum = 0

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            if self.center <= 1400:
                self.center += self.ai_settings.shipSpeed
        if self.moving_left:
            if self.center >= 0:
                self.center -= self.ai_settings.shipSpeed

        self.rect.centerx = self.center

    def blitShip(self):

        if self.type == 1:
            self.deathnum += 1
            if self.deathnum <= 20:
                self.image = self.expo[0]
            elif self.deathnum <= 40:
                self.image = self.expo[1]
            elif self.deathnum <= 60:
                self.image = self.expo[2]
            elif self.deathnum <= 80:
                self.image = self.expo[3]
            else:
                self.type = 2
        self.screen.blit(self.image, self.rect)

    def shipCenter(self):
        self.center = self.screen_rect.centerx