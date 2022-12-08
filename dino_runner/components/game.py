import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.center_width = SCREEN_WIDTH // 2
        self.center_height = SCREEN_HEIGHT // 2
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.running = True
        self.score = 0
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running: 
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.obstacle_manager.reset_obstacles()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def update_score(self):
        self.score +=1
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        my_score = f'Score: {self.score}'
        self.display_message(my_score, 100, 50, 1)

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def display_message(self, item, width, height, background):
            if background == 0:
                self.screen.fill((255, 255, 255))
                font = pygame.font.Font(FONT_STYLE, 30)
                text = font.render(item, True, (0,0,0))
                text_rect = text.get_rect()
                text_rect.center = (width, height)
                self.screen.blit(text, text_rect)
            else:
                font = pygame.font.Font(FONT_STYLE, 30)
                text = font.render(item, True, (0,0,0))
                text_rect = text.get_rect()
                text_rect.center = (width, height)
                self.screen.blit(text, text_rect)
            

    def show_menu(self):
        print(self.death_count)
        menu_str = "Press any key to start"
        if self.death_count == 0:
            self.display_message(menu_str, self.center_width, self.center_height, 0)
            
        else:
            self.display_message("You have died", self.center_width, self.center_height - 40, 0)
            self.display_message("Want to play again? ", self.center_width, self.center_height + 10, 1)


        pygame.display.update()
        self.handle_events_on_menu()
