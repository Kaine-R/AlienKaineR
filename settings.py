import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1400
        self.screen_height = 700
        self.bg_color = (20, 20, 50)

        self.gameSpeed = 1

        self.shipSpeed = 1.8
        self.alienSpeed = 1.4
        self.alienDirection = 1
        self.fleetDrop = 10

        self.bulletSpeed = 2
        # self.image = pygame.image.load("images/basicShot.png")
        # self.bulletRect = pygame.image.get_rect()
        self.bulletWidth = 4
        self.bulletHeight = 10
        self.bulletColor = 250, 250, 250

        self.timer = 0
        self.frameChange = 1000