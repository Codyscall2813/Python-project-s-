import random
import pygame
from pathlib import Path
from time import sleep

class CarRacing:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.screen = None
        self.asset_path = Path(__file__).parent / "img"
        
        # Load icon and set display icon
        self.load_assets()
        pygame.display.set_icon(self.icon_image)
        
        # Start the game
        self.start_game()

    def load_assets(self):
        try:
            # Load images
            self.car_image = pygame.image.load(self.asset_path / "car.png")
            self.enemy_car_image = pygame.image.load(self.asset_path / "enemy_car_2.png")
            self.background_image = pygame.image.load(self.asset_path / "back_ground.jpg")
            self.icon_image = pygame.image.load(self.asset_path / "icon.png")
        except FileNotFoundError as e:
            print(f"Error loading images: {e}")
            pygame.quit()
            exit()

    def setup_game(self):
        self.is_crashed = False
        self.car_x = self.screen_width * 0.45
        self.car_y = self.screen_height * 0.8
        self.car_width = 49

        # Enemy car setup
        self.enemy_car_x = random.randrange(310, 450)
        self.enemy_car_y = -600
        self.enemy_car_speed = 5
        self.enemy_car_width = 49
        self.enemy_car_height = 100

        # Background setup
        self.bg_x1 = (self.screen_width / 2) - (360 / 2)
        self.bg_x2 = self.bg_x1
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 3
        self.score = 0

    def draw_car(self):
        self.screen.blit(self.car_image, (self.car_x, self.car_y))

    def start_game(self):
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Car Race')
        self.setup_game()
        self.run_game()

    def run_game(self):
        while not self.is_crashed:
            self.handle_events()
            self.update_game_state()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.car_x -= 50
                elif event.key == pygame.K_RIGHT:
                    self.car_x += 50

    def update_game_state(self):
        self.enemy_car_y += self.enemy_car_speed

        if self.enemy_car_y > self.screen_height:
            self.enemy_car_y = -self.enemy_car_height
            self.enemy_car_x = random.randrange(310, 450)

        if self.detect_collision() or self.car_x < 310 or self.car_x > 460:
            self.is_crashed = True
            self.display_message("Game Over !!!")

        if self.score % 100 == 0 and self.score != 0:
            self.enemy_car_speed += 1
            self.bg_speed += 1

        self.score += 1

    def detect_collision(self):
        return (
            self.car_y < self.enemy_car_y + self.enemy_car_height and
            (
                (self.car_x > self.enemy_car_x and self.car_x < self.enemy_car_x + self.enemy_car_width) or
                (self.car_x + self.car_width > self.enemy_car_x and self.car_x + self.car_width < self.enemy_car_x + self.enemy_car_width)
            )
        )

    def render(self):
        self.screen.fill(self.black)
        self.render_background()
        self.screen.blit(self.enemy_car_image, (self.enemy_car_x, self.enemy_car_y))
        self.draw_car()
        self.display_score()
        pygame.display.update()

    def render_background(self):
        self.screen.blit(self.background_image, (self.bg_x1, self.bg_y1))
        self.screen.blit(self.background_image, (self.bg_x2, self.bg_y2))

        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.screen_height:
            self.bg_y1 = -600

        if self.bg_y2 >= self.screen_height:
            self.bg_y2 = -600

    def display_message(self, message):
        font = pygame.font.SysFont("comicsansms", 72, True)
        text = font.render(message, True, (255, 255, 255))
        self.screen.blit(text, (self.screen_width // 2 - text.get_width() // 2, self.screen_height // 2 - text.get_height() // 2))
        self.display_credit()
        pygame.display.update()
        self.clock.tick(60)
        sleep(1)
        self.setup_game()
        self.run_game()

    def display_score(self):
        font = pygame.font.SysFont("lucidaconsole", 20)
        text = font.render(f"Score: {self.score}", True, self.white)
        self.screen.blit(text, (0, 0))

    def display_credit(self):
        font = pygame.font.SysFont("lucidaconsole", 14)
        credits = ["Thanks For Playing!"]
        for i, line in enumerate(credits):
            text = font.render(line, True, self.white)
            self.screen.blit(text, (600, 520 + i * 20))

if __name__ == '__main__':
    CarRacing()
