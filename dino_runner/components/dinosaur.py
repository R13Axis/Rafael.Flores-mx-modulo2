import pygame
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD

DUCK_IMG = {DEFAULT_TYPE : DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE : JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
RUN_IMG = {DEFAULT_TYPE : RUNNING, SHIELD_TYPE: RUNNING_SHIELD}


class Dinosaur:
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 80
        self.dino_rect.y = 310
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = 8.5
        self.has_power_up = False
        self.power_time_up = 0
        self.jump_sound = pygame.mixer.Sound("dino_runner/assets/sounds/audiomass-output.mp3")
    
    def update(self, user_input):
        
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
            
        if user_input[pygame.K_UP] and not self.dino_jump and not self.dino_duck:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = True
            self.jump_sound.play()
            
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

        if user_input[pygame.K_DOWN] and not self.dino_jump: 
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False 

        elif not self.dino_duck:
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

        if self.step_index >=9:
            self.step_index = 0

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.dino_rect.y -= self.jump_vel * 4
        self.jump_vel -= 0.8
        
        if self.jump_vel < -8.5:
            self.dino_rect.y = 310
            self.dino_jump = False
            self.jump_vel = 8.5
        
    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect.x = 80
        self.dino_rect.y = 310
        self.step_index += 1
    
    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect.x = 80
        self.dino_rect.y = 340
        self.step_index +=1
        

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))