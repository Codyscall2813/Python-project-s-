import pygame
import time
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
SNAKE_BLOCK = 10
SNAKE_SPEED = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Font styles
font_style = pygame.font.SysFont("calibri", 50)
score_font = pygame.font.SysFont("calibri", 20)

class SnakeGame:
    def __init__(self):
        self.game_over = False
        self.snake_list = []
        self.length_of_snake = 1
        self.x1 = WIDTH / 2
        self.y1 = HEIGHT / 2
        self.x1_change = 0
        self.y1_change = 0
        self.foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
        self.foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
        self.start_game = False
        self.last_score = -1  # To keep track of the last printed score

    def draw_snake(self):
        for segment in self.snake_list:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])

    def display_score(self):
        current_score = self.length_of_snake - 1
        if current_score != self.last_score:
            sys.stdout.write(f"\rScore: {current_score}")
            sys.stdout.flush()
            self.last_score = current_score
        
        score_text = score_font.render(f"Your Score: {current_score}", True, BLACK)
        screen.blit(score_text, [0, 0])

    def game_message(self, msg, color):
        message = font_style.render(msg, True, color)
        screen.blit(message, [WIDTH / 6, HEIGHT / 3])
        print(msg)  # Print game message to terminal

    def display_instructions(self):
        screen.fill(WHITE)
        instruction_text = font_style.render("Press an Arrow Key to Start", True, BLACK)
        text_width, text_height = instruction_text.get_size()
        x = (WIDTH - text_width) / 2
        y = (HEIGHT - text_height) / 2
        screen.blit(instruction_text, (x, y))
        pygame.display.update()


    def run_game(self):
        # Display instructions screen
        self.display_instructions()
        
        # Wait for user to press an arrow key to start the game
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                        waiting = False

        while not self.game_over:
            while self.game_over:
                screen.fill(BLACK)
                self.game_message("You Lost!", RED)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            quit()
                        if event.key == pygame.K_c:
                            self.__init__()
                            self.run_game()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.x1_change == 0:
                        self.x1_change = -SNAKE_BLOCK
                        self.y1_change = 0
                    elif event.key == pygame.K_RIGHT and self.x1_change == 0:
                        self.x1_change = SNAKE_BLOCK
                        self.y1_change = 0
                    elif event.key == pygame.K_UP and self.y1_change == 0:
                        self.y1_change = -SNAKE_BLOCK
                        self.x1_change = 0
                    elif event.key == pygame.K_DOWN and self.y1_change == 0:
                        self.y1_change = SNAKE_BLOCK
                        self.x1_change = 0

            if self.x1 >= WIDTH or self.x1 < 0 or self.y1 >= HEIGHT or self.y1 < 0:
                self.game_over = True

            self.x1 += self.x1_change
            self.y1 += self.y1_change
            screen.fill(WHITE)
            pygame.draw.rect(screen, BLACK, [self.foodx, self.foody, SNAKE_BLOCK, SNAKE_BLOCK])

            snake_head = [self.x1, self.y1]
            self.snake_list.append(snake_head)
            if len(self.snake_list) > self.length_of_snake:
                del self.snake_list[0]

            if snake_head in self.snake_list[:-1]:
                self.game_over = True

            self.draw_snake()
            self.display_score()
            pygame.display.update()

            if self.x1 == self.foodx and self.y1 == self.foody:
                self.foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
                self.foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
                self.length_of_snake += 1

            clock.tick(SNAKE_SPEED)

        pygame.quit()
        quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()
