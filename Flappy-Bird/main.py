# Importing the libraries
import pygame
import sys
import random

# Initializing pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 350, 622
FPS = 120
GRAVITY = 0.17
BIRD_FLAP_EVENT = pygame.USEREVENT
CREATE_PIPE_EVENT = pygame.USEREVENT + 1
PIPE_MOVE_SPEED = 3
FLOOR_MOVE_SPEED = 1
PIPE_HEIGHT_OPTIONS = [400, 350, 533, 490]
FONT_SIZE = 27

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
icon_image = pygame.image.load("Collection/Flappy-Bird/imgs/icon.png")
pygame.display.set_icon(icon_image)


# Load images
background_image = pygame.image.load("Collection/Flappy-Bird/imgs/img_46.png")
floor_image = pygame.image.load("Collection/Flappy-Bird/imgs/img_50.png")
bird_images = {
    "up": pygame.image.load("Collection/Flappy-Bird/imgs/img_47.png"),
    "down": pygame.image.load("Collection/Flappy-Bird/imgs/img_48.png"),
    "mid": pygame.image.load("Collection/Flappy-Bird/imgs/img_49.png")
}
pipe_image = pygame.image.load("Collection/Flappy-Bird/imgs/greenpipe.png")
game_over_image = pygame.image.load("Collection/Flappy-Bird/imgs/img_45.png").convert_alpha()

# Set up bird
bird_index = 0
pygame.time.set_timer(BIRD_FLAP_EVENT, 200)
current_bird_image = bird_images["mid"]
bird_rect = current_bird_image.get_rect(center=(67, SCREEN_HEIGHT // 2))
bird_movement = 0

# Set up pipes
pipes = []
pygame.time.set_timer(CREATE_PIPE_EVENT, 1200)

# Set up scores
current_score = 0
high_score = 0
score_update_time = True
score_font = pygame.font.Font("Collection/Flappy-Bird/Mali-Regular.ttf", FONT_SIZE)

# Set up floor
floor_x_position = 0

# Initialize clock
clock = pygame.time.Clock()

# Helper functions
def draw_floor():
    screen.blit(floor_image, (floor_x_position, SCREEN_HEIGHT - 72))
    screen.blit(floor_image, (floor_x_position + 448, SCREEN_HEIGHT - 72))

def create_pipe_pair():
    pipe_y = random.choice(PIPE_HEIGHT_OPTIONS)
    top_pipe_rect = pipe_image.get_rect(midbottom=(467, pipe_y - 300))
    bottom_pipe_rect = pipe_image.get_rect(midtop=(467, pipe_y))
    return top_pipe_rect, bottom_pipe_rect

def animate_pipes():
    global game_over
    for pipe_rect in pipes:
        if pipe_rect.top < 0:
            flipped_pipe_image = pygame.transform.flip(pipe_image, False, True)
            screen.blit(flipped_pipe_image, pipe_rect)
        else:
            screen.blit(pipe_image, pipe_rect)

        pipe_rect.centerx -= PIPE_MOVE_SPEED
        if pipe_rect.right < 0:
            pipes.remove(pipe_rect)

        if bird_rect.colliderect(pipe_rect):
            game_over = True

def draw_score(game_state):
    if game_state == "playing":
        score_text = score_font.render(str(current_score), True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 66))
        screen.blit(score_text, score_rect)
    elif game_state == "game_over":
        score_text = score_font.render(f"Score: {current_score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 66))
        screen.blit(score_text, score_rect)

        high_score_text = score_font.render(f"High Score: {high_score}", True, (255, 255, 255))
        high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH // 2, 506))
        screen.blit(high_score_text, high_score_rect)

def update_score():
    global current_score, score_update_time, high_score
    if pipes:
        for pipe_rect in pipes:
            if 65 < pipe_rect.centerx < 69 and score_update_time:
                current_score += 1
                score_update_time = False
            if pipe_rect.left <= 0:
                score_update_time = True

    if current_score > high_score:
        high_score = current_score

# Main game loop
running = True
game_over = False
while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    bird_movement = -7
                else:
                    game_over = False
                    pipes.clear()
                    bird_movement = 0
                    bird_rect = current_bird_image.get_rect(center=(67, SCREEN_HEIGHT // 2))
                    score_update_time = True
                    current_score = 0

        if event.type == BIRD_FLAP_EVENT:
            bird_index = (bird_index + 1) % len(bird_images)
            current_bird_image = list(bird_images.values())[bird_index]
            bird_rect = current_bird_image.get_rect(center=bird_rect.center)

        if event.type == CREATE_PIPE_EVENT:
            pipes.extend(create_pipe_pair())

    # Game logic
    if not game_over:
        bird_movement += GRAVITY
        bird_rect.centery += bird_movement
        rotated_bird_image = pygame.transform.rotozoom(current_bird_image, bird_movement * -6, 1)

        if bird_rect.top < 5 or bird_rect.bottom >= SCREEN_HEIGHT - 72:
            game_over = True

        screen.blit(background_image, (0, 0))
        screen.blit(rotated_bird_image, bird_rect)
        animate_pipes()
        update_score()
        draw_score("playing")
    else:
        screen.blit(background_image, (0, 0))
        screen.blit(game_over_image, game_over_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
        draw_score("game_over")

    floor_x_position -= FLOOR_MOVE_SPEED
    if floor_x_position < -448:
        floor_x_position = 0

    draw_floor()
    pygame.display.update()

pygame.quit()
sys.exit()
