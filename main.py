import sys
import pygame
from pygame.sprite import Group
import pygame.mixer
from settings import Settings
from ship import Ship
from alien import Alien
from gameStats import GameStats
from button import Button
from score import Score
from badBullets import BadBullets
from highScores import HighScores
from background import Background
from barrier import Barrier

import gameFunctions as gf
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 50)
# sets the window placement

def run_game():

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("images/music.mp3")
    pygame.mixer.music.play(-1, 130.0)
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Aliens")
    stats = GameStats(ai_settings)
    playButton = Button(ai_settings, screen, "Play")
    highScore = HighScores(screen, ai_settings)
    score = Score(ai_settings, screen, "Wave#: " + str(stats.waveNumber), stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stars = Group()
    badBullets = Group()
    barriers = Group()
    gf.makeBarriers(barriers, screen, ai_settings)
    gf.createFleet(ai_settings, screen, ship, aliens)
    highScore.prepScores()

    screen.fill(ai_settings.bg_color)
    while True:
        screen.fill(ai_settings.bg_color)
        gf.updateBackground(ai_settings, screen, stars)
        gf.drawBarrier(barriers)
        gf.check_events(ai_settings, screen, ship, stats, playButton, aliens, bullets, barriers)
        gf.updateScreen(ai_settings, screen, stats, ship, aliens, bullets, playButton, score, badBullets)


        if stats.gameActive:
            ship.update()
            gf.barriersCollide(barriers, bullets)
            gf.updateBullets(ai_settings, screen, stats, ship, aliens, bullets, badBullets, highScore, barriers)
            gf.updateAliens(ai_settings, stats, screen, ship, aliens, bullets, highScore, badBullets)
            gf.badShotting(aliens, badBullets, ai_settings, screen)
        else:
            highScore.prepScores()
            highScore.drawScores()

        pygame.display.flip()


run_game()