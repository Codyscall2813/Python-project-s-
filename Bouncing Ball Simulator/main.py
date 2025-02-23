import pygame
import time
import random

pygame.init()

# Setting screen size of pygame window to 800 by 600 pixels
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load(r'Collection\Bouncing_ball_simulator\imgs\background-img.jpg')

# Adding title
pygame.display.set_caption('Ball Bounce Simulation')
icon = pygame.image.load(r'Collection\Bouncing_ball_simulator\imgs\icon.png')
pygame.display.set_icon(icon)

class Ball:
    ball_image = pygame.image.load(r'Collection\Bouncing_ball_simulator\imgs\ball.png')
    gravity = 1

    def __init__(self):
        self.velocity_x = 4
        self.velocity_y = 4
        self.x = random.randint(0, 768)
        self.y = random.randint(0, 350)

    def render(self):
        screen.blit(Ball.ball_image, (self.x, self.y))

    def move(self):
        # Changing y component of velocity due to downward acceleration
        self.velocity_y += Ball.gravity
        # Changing position based on velocity
        self.x += self.velocity_x
        self.y += self.velocity_y
        # Collision with the walls lead to change in velocity
        if self.x < 0 or self.x > 768:
            self.velocity_x *= -1
        if self.y < 0 and self.velocity_y < 0:
            self.velocity_y *= -1
            self.y = 0
        if self.y > 568 and self.velocity_y > 0:
            self.velocity_y *= -1
            self.y = 568

# List of Ball objects created
balls = [Ball() for _ in range(5)]

# The main program loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    time.sleep(0.02)
    screen.blit(background, (0, 0))
    for ball in balls:
        ball.render()
        ball.move()
    pygame.display.update()

pygame.quit()
