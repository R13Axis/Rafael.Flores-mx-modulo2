
import random
import pygame
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus, Large

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        turn = random.randint(0, 2)
        if len(self.obstacles) == 0:
            if turn == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(Large(LARGE_CACTUS))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    