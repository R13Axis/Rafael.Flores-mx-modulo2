
import random
import pygame
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SHIELD_TYPE
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.death_sound = pygame.mixer.Sound("dino_runner/assets/sounds/car-output.mp3")

    def update(self, game):
        turn = random.randint(0, 2)
        if len(self.obstacles) == 0:
            if turn == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif turn == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS, 305))
            else:
                self.obstacles.append(Bird(BIRD))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type != SHIELD_TYPE:
                    game.playing = False
                    game.death_count += 1
                    self.death_sound.play()
                    game.reset_score()
                    game.draw_death_count()
                    break

                else: 
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
    