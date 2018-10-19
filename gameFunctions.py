import sys
import pygame
import random
from bullet import Bullet
from alien import Alien
from time import sleep
from background import Background
from barrier import Barrier
from badBullets import BadBullets

def check_events(ai_settings, screen, ship, stats, playButton, aliens, bullets, barriers):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDown(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            checkKeyUp(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            if checkPlayButton(playButton, stats, mouseX, mouseY):
              resetGame(ai_settings, screen, ship, aliens, bullets, barriers)


def checkKeyDown(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        newBullet = Bullet(ai_settings, screen, ship)
        bullets.add(newBullet)

def checkKeyUp(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def checkPlayButton(playButton, stats, mouseX, mouseY):
    if playButton.rect.collidepoint(mouseX, mouseY):
        stats.waveNumber = 1
        stats.gameActive = True
        return True
    else:
        return False

def scorePoint(stats):
    stats.waveNumber += 1

def badShotting(aliens, badBullets, ai_settings, screen):
    for alien in aliens.sprites():
        if random.randint(0, 10000) < 8:
            newBullet = BadBullets(ai_settings, screen, alien)
            badBullets.add(newBullet)

def updateScreen(ai_settings, screen, stats, ship, aliens, bullets, playButton, score, badBullets):
    if not stats.gameActive:
        playButton.drawButton()
    if (random.randint(0, 10000) <= 15):
        newUFO = Alien(ai_settings, screen)
        newUFO.ufo()
        aliens.add(newUFO)

    for bullets in bullets.sprites():
        bullets.drawBullet()
    for bullets in badBullets.sprites():
        bullets.drawBullet()
    score.prepScore("Wave#: " + str(stats.waveNumber), stats)
    score.drawScore()
    ship.blitShip()

    for alien in aliens.sprites():
        alien.blitAliens(ai_settings)
    #aliens.draw(screen)

def updateBullets(ai_settings, screen, stats, ship, aliens, bullets, badBullets, highScores, barriers):
    bullets.update()
    for alien in aliens.sprites():
        if alien.type != 4 and pygame.sprite.spritecollide(alien, bullets, True):
            stats.score += 50 * stats.waveNumber
            alien.type = 4

    if pygame.sprite.spritecollide(ship, badBullets, True):
        ship.type = 1

    if ship.type == 2:
        shipHit(ai_settings, stats, screen, ship, aliens, bullets, highScores, badBullets)


    for barrier in barriers:
        if pygame.sprite.spritecollide(barrier, badBullets, True):
            barrier.update(barriers)

    if len(aliens) == 0:
        createFleet(ai_settings, screen, ship, aliens)
        scorePoint(stats)
        ai_settings.gameSpeed += .25

    badBullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
#     print(len(bullets))

def updateBackground(ai_settings, screen, stars):
    stars.update()
    screenRect = screen.get_rect()
    if(random.randint(0, 10) < 6):
        newStar = Background(ai_settings, screen)
        stars.add(newStar)
    for star in stars.copy():
        if star.y >= screenRect.bottom:
            stars.remove(star)
    for star in stars.sprites():
        star.createStar()


def createFleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    ytemp = alien.rect.height
    for p in range(3):
        for j in range(2):
            for i in range(number_aliens_x):
                alien = Alien(ai_settings, screen)
                alien.x = alien_width + 2 * alien_width * i
                alien.rect.x = alien.x
                alien.rect.y = ytemp
                alien.type = p
                aliens.add(alien)
            ytemp += 1.5 * alien.rect.height

def updateAliens(ai_settings, stats, screen, ship, aliens, bullets, highScore, badBullets):
    checkFleet(ai_settings, aliens)
    if pygame.sprite.spritecollideany(ship, aliens):
        shipHit(ai_settings, stats, screen, ship, aliens, bullets, highScore, badBullets)
    checkFleetHeight(screen, aliens)
    aliens.update()

def checkFleet(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.checkEdges():
            changeFleetDirection(ai_settings, aliens)
            break

def changeFleetDirection(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleetDrop
    ai_settings.alienDirection *= -1

def shipHit(ai_settings, stats, screen, ship, aliens, bullets, highScore, badBullets):
    bullets.empty()
    ship.shipCenter()
    badBullets.empty()
    sleep(0.5)
    stats.gameActive = False
    ship.type = 0
    ship.deathnum = 0
    ship.image = ship.normalImage
    ai_settings.gameSpeed = 1
    settingsHighScores(stats, highScore)

def settingsHighScores(stats, highScore):
    if stats.score > highScore.highScore1:
        highScore.highScore3 = highScore.highScore2
        highScore.highScore2 = highScore.highScore1
        highScore.highScore1 = stats.score
    elif stats.score > highScore.highScore2:
        highScore.highScore3 = highScore.highScore2
        highScore.highScore2 = highScore.highScore1
        highScore.highScore2 = stats.score
    elif stats.score > highScore.highScore3:
        highScore.highScore3 = stats.score
    stats.score = 0

def checkFleetHeight(screen, aliens):
    screenRect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.top >= screenRect.bottom:
            alien.rect.y = -30

def resetGame(ai_settings, screen, ship, aliens, bullets, barriers):
    aliens.empty()
    bullets.empty()
    barriers.empty()
    ship.shipCenter()
    createFleet(ai_settings, screen, ship, aliens)
    makeBarriers(barriers, screen, ai_settings)

def makeBarriers(barriers, screen, ai_settings):
    xTemp = ai_settings.screen_width/4 - 40
    yTemp = 4 * ai_settings.screen_height/5
    for j in range(3):
        for n in range(2):
            for i in range(7):
                newBarrier = Barrier(screen, ai_settings)
                newBarrier.rect.x = xTemp + (i*10)
                newBarrier.rect.y = yTemp + (20*n)
                barriers.add(newBarrier)
        xTemp += ai_settings.screen_width/4

def barriersCollide(barriers, bullets):
    for barrier in barriers:
        if pygame.sprite.spritecollide(barrier, bullets, dokill=True):
            barrier.update(barriers)

def drawBarrier(barriers):
    for barrier in barriers.sprites():
        barrier.drawBarrier()
