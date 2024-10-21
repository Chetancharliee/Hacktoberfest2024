import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
display_width = 600
display_height = 400

# Create the display window
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Set game clock (FPS)
clock = pygame.time.Clock()

# Define snake properties
snake_block = 10
snake_speed = 15

# Define fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the current score
def show_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    game_display.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_display, green, [block[0], block[1], snake_block, snake_block])

# Function to display messages on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [display_width / 6, display_height / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = display_width / 2
    y1 = display_height / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Place the first food
    food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    # Main game loop
    while not game_over:

        while game_close:
            game_display.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            show_score(length_of_snake - 1)
            pygame.display.update()

            # Check for player input to restart or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Check for player input to move the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if the snake hits the boundaries
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_display.fill(black)

        # Draw the food
        pygame.draw.rect(game_display, blue, [food_x, food_y, snake_block, snake_block])

        # Add the new snake position to the list
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake collides with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Draw the snake
        draw_snake(snake_block, snake_list)
        show_score(length_of_snake - 1)

        # Update the display
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Control the speed of the game
        clock.tick(snake_speed)

    # Quit the game
    pygame.quit()
    quit()

# Run the game
game_loop()
