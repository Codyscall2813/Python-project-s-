import pygame
import sys
import random

# Initializing pygame
pygame.init()

# Frames per second
clock = pygame.time.Clock()

# Window parameters
width = 800
height = 500

# Creating the window
screen = pygame.display.set_mode((width, height))

# Setting the title and icon
pygame.display.set_caption("Hangman")
icon = pygame.image.load("img_9.png")
pygame.display.set_icon(icon)

# Global variables
hangman_status = 0
word = ""
guessed = []
buttons = []
game_over = False
image = pygame.image.load("img_21.png")  # Initialize the image variable

def reset_game():
    global hangman_status, word, guessed, buttons, game_over, image
    hangman_status = 0
    words = [
    'NUMPY', 'PANDAS', 'MATPLOTLIB', 'SCI-KIT LEARN', 'FLASK', 'DJANGO', 
    'JUPYTER', 'TENSORFLOW', 'KERAS', 'PYTORCH', 'RECURSION', 'DEBUGGING', 
    'ALGORITHMS', 'DATA SCIENCE', 'WEB SCRAPING', 'APIs', 'PYTHONIC', 'SCRIPTS', 
    'OOP', 'FUNCTIONS', 'VARIABLES', 'LOOPS', 'CONDITIONS'
]
    word = random.choice(words)
    guessed = []
    buttons = []
    A = 65
    for ind, box in enumerate(boxes):
        letter = chr(A + ind)
        button = [box, letter]
        buttons.append(button)
    game_over = False
    image = pygame.image.load("img_21.png")  # Reset the image to the initial one

# Game over screen
def game_over_screen():
    global game_text
    screen.fill((255, 255, 255))
    text = game_font.render(game_text, True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(3000)  # Display the game over message for 3 seconds

# To draw boxes
def draw_buttons(buttons):
    for box, letter in buttons:
        btn_text = font.render(letter, True, (0, 0, 0))
        btn_rect = btn_text.get_rect(center=(box.x + size // 2, box.y + size // 2))
        screen.blit(btn_text, btn_rect)
        pygame.draw.rect(screen, (0, 0, 0), box, 2)

# To display the word
def display_guess():
    display_text = ''
    for letter in word:
        if letter in guessed:
            display_text += f"{letter} "
        else:
            display_text += '_ '

    text = letter_font.render(display_text, True, (0, 0, 0))
    screen.blit(text, (400, 200))

images = []
row = 2
col = 13
gap = 20
size = 40
boxes = []

# To draw boxes
for row in range(row):
    for col in range(col):
        x = ((col * gap) + gap) + (size * col)
        y = ((row * gap) + gap) + (size * row) + 330
        box = pygame.Rect(x, y, size, size)
        boxes.append(box)

buttons = []
A = 65

# To display alphabets
for ind, box in enumerate(boxes):
    letter = chr(A + ind)
    button = [box, letter]
    buttons.append(button)

# setting the font style
font = pygame.font.SysFont("arial", 30)
game_font = pygame.font.SysFont("arial", 80)
letter_font = pygame.font.SysFont("arial", 60)

# Title parameters
title = "Hangman"
title_text = game_font.render(title, True, (0, 0, 0))
title_rect = title_text.get_rect(center=(width // 2, title_text.get_height() // 2 + 10))

# Initialize the game
reset_game()

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))
    if not game_over:
        # Checking for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quit event
                running = False
            # Checking for mouse position
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = event.pos

                # Checking for correct letter
                for button, letter in buttons:
                    if button.collidepoint(click_pos):
                        if letter not in word:
                            hangman_status += 1
                        if hangman_status == 6:
                            game_text = "YOU LOST!"
                            game_over = True
                        guessed.append(letter)
                        buttons.remove([button, letter])

                # displaying the images accordingly
                if hangman_status == 1:
                    image = pygame.image.load("img_23.png")
                elif hangman_status == 2:
                    image = pygame.image.load("img_22.png")
                elif hangman_status == 3:
                    image = pygame.image.load("img_24.png")
                elif hangman_status == 4:
                    image = pygame.image.load("img_25.png")
                elif hangman_status == 5:
                    image = pygame.image.load("img_26.png")
                elif hangman_status == 6:
                    game_text = "YOU LOST!"
                    game_over = True

        screen.blit(image, (150, 150))
        for box in boxes:
            pygame.draw.rect(screen, (0, 0, 0), box, 2)

        # Win and Lost
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
        if won:
            game_text = "YOU WON!"
            game_over = True

        draw_buttons(buttons)
        display_guess()
        screen.blit(title_text, title_rect)
        clock.tick(50)
        pygame.display.update()

    else:
        game_over_screen()
        pygame.quit()
        sys.exit()

pygame.quit()
