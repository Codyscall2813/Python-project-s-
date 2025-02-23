import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Frames per second
fps_clock = pygame.time.Clock()

# Dimensions for window
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

# Create game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Title and icon
pygame.display.set_caption("Ping Pong Game")

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game objects
ball = pygame.Rect(WINDOW_WIDTH / 2 - 15, WINDOW_HEIGHT / 2 - 15, 30, 30)
player1_paddle = pygame.Rect(WINDOW_WIDTH - 20, WINDOW_HEIGHT / 2 - 70, 10, 140)
player2_paddle = pygame.Rect(10, WINDOW_HEIGHT / 2 - 70, 10, 140)

# Game variables
ball_speed_x = 6 * random.choice((1, -1))
ball_speed_y = 6 * random.choice((1, -1))
player1_speed = 0
player2_speed = 6
player1_score = 0
player2_score = 0
game_started = False

# Font for score display and instructions
font = pygame.font.SysFont("calibri", 25)
font_style = pygame.font.SysFont("calibri", 50)

# Function for ball movement
def move_ball():
    global ball_speed_x, ball_speed_y, player1_score, player2_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce the ball off the top and bottom
    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        ball_speed_y *= -1

    # Check for scoring
    if ball.left <= 0:
        player2_score += 1
        reset_ball()
    if ball.right >= WINDOW_WIDTH:
        player1_score += 1
        reset_ball()

    # Bounce the ball off paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed_x *= -1

# Function for player 1 paddle movement
def move_player1():
    global player1_speed
    player1_paddle.y += player1_speed
    if player1_paddle.top < 0:
        player1_paddle.top = 0
    if player1_paddle.bottom > WINDOW_HEIGHT:
        player1_paddle.bottom = WINDOW_HEIGHT

# Function for player 2 paddle movement
def move_player2():
    if player2_paddle.top < ball.y:
        player2_paddle.top += player2_speed
    if player2_paddle.bottom > ball.y:
        player2_paddle.bottom -= player2_speed
    if player2_paddle.top < 0:
        player2_paddle.top = 0
    if player2_paddle.bottom > WINDOW_HEIGHT:
        player2_paddle.bottom = WINDOW_HEIGHT

# Function to reset the ball position
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

# Function to display instructions
def display_instructions():
    screen.fill(WHITE)
    instruction_text = font_style.render("Press an Arrow Key to Start", True, BLACK)
    text_width, text_height = instruction_text.get_size()
    x = (WINDOW_WIDTH - text_width) / 2
    y = (WINDOW_HEIGHT - text_height) / 2
    screen.blit(instruction_text, (x, y))
    pygame.display.update()

# Game Loop
while True:
    for event in pygame.event.get():
        # Handle quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 8
            if event.key == pygame.K_UP:
                player1_speed -= 8
            if event.key in [pygame.K_DOWN, pygame.K_UP] and not game_started:
                game_started = True

        # Handle key release events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 8
            if event.key == pygame.K_UP:
                player1_speed += 8

    # Show instructions if the game hasn't started
    if not game_started:
        display_instructions()
        continue

    # Update game objects
    move_ball()
    move_player1()
    move_player2()

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (220, 220, 220), player1_paddle)
    pygame.draw.rect(screen, (220, 220, 220), player2_paddle)
    pygame.draw.ellipse(screen, RED, ball)
    pygame.draw.aaline(screen, (220, 220, 220), (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT))

    # Draw scores
    player1_score_text = font.render("Score: " + str(player1_score), False, (255, 255, 255))
    screen.blit(player1_score_text, [600, 50])
    player2_score_text = font.render("Score: " + str(player2_score), False, (255, 255, 255))
    screen.blit(player2_score_text, [300, 50])

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    fps_clock.tick(60)
