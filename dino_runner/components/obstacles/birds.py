import random 
from dino_runner.components.obstacles.obstacle import Obstacles

class Bird(Obstacles):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = self.radio()
        self.index = 0
        

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1

    def radio(self):
        return random.randint(200, 290)

    