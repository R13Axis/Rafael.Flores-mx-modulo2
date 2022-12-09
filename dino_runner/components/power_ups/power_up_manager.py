import pygame
import random
from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.duration = random.randint(4, 8)

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            self.power_ups.append(Shield())

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.get_ticks()
                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.powe_time_up = power_up.start_time + (self.duration * 1000)
                self.power_ups.remove(power_up)
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.drw(screen)
            
    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)