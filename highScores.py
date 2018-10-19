import pygame.font


class HighScores():
    def __init__(self, screen, settings):
        self.screen = screen
        self.ai_settings = settings

        self.highScore1, self.highScore2, self.highScore3 = 13225, 2050, 2000

        self.font = pygame.font.SysFont(None, 30)
        self.fontTitle = pygame.font.SysFont(None, 48)
        self.textColor = (20, 20, 20)
        self.boxColor = (130, 100, 100)

        self.rect1, self.rect2 = pygame.Rect(50, 50, 300, 150), pygame.Rect(50, 50, 300, 40)

    def prepScores(self):
        self.imageTitle = self.fontTitle.render("HIGHSCORES", True, self.textColor)
        self.imageTitleRect = self.imageTitle.get_rect()
        self.imageTitleRect.x, self.imageTitleRect.y = 55, 55
        self.image1 = self.font.render("HighScore 1: " + str(self.highScore1), True, self.textColor)
        self.image2 = self.font.render("HighScore 2: " + str(self.highScore2), True, self.textColor)
        self.image3 = self.font.render("HighScore 3: " + str(self.highScore3), True, self.textColor)
        self.imageRect1, self.imageRect2, self.imageRect3 = self.image1.get_rect(), self.image2.get_rect(), self.image3.get_rect()
        self.imageRect1.x, self.imageRect1.y = 55, 100
        self.imageRect2.x, self.imageRect2.y = 55, 130
        self.imageRect3.x, self.imageRect3.y = 55, 160


    def drawScores(self):
        self.screen.fill((140, 100, 100), self.rect1)
        self.screen.fill((100, 100, 100), self.rect2)
        self.screen.blit(self.image1, self.imageRect1)
        self.screen.blit(self.image2, self.imageRect2)
        self.screen.blit(self.image3, self.imageRect3)
        self.screen.blit(self.imageTitle, self.imageTitleRect)


