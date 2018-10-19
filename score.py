import pygame.font

class Score():
    def __init__(self, ai_settings, screen, msg, stats):
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.width, self.height = 200, 50
        self.scoreColor = (0, 200, 200)
        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.prepScore(msg, stats)
        self.rect2 = pygame.Rect(0, 0, self.width, self.height)



    def drawScore(self):
        # self.screen.fill(self.scoreColor, self.rect)
        self.screen.blit(self.msgImage, self.msgImageRect)
        self.screen.blit(self.msgImage2, self.msgImageRect2)

    def prepScore(self, msg, stats):
        self.msgImage = self.font.render(msg, True, self.textColor, self.scoreColor)
        self.msgImageRect = self.msgImage.get_rect()
        self.msgImageRect.x = self.screenRect.right - self.width
        self.msgImageRect.y = self.screenRect.top + 25

        self.msgImage2 = self.font.render("Score: " + str(stats.score), True, self. textColor, self.scoreColor)
        self.msgImageRect2 = self.msgImage2.get_rect()
        self.msgImageRect2.x = self.msgImageRect.x
        self.msgImageRect2.y = self.msgImageRect.y + self.height

