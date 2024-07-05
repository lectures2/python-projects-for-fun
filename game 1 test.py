import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Set up the snake
snake_block_size = 20
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def our_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block_size, snake_block_size])

def game_loop():
    game_over = False
    game_quit = False

    # Snake initial position
    x1 = display_width / 2
    y1 = display_height / 2

    # Snake movement
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Randomly place food
    food_x = round(random.randrange(0, display_width - snake_block_size) / 20) * 20
    food_y = round(random.randrange(0, display_height - snake_block_size) / 20) * 20

    while not game_quit:
        while game_over == True:
            game_display.fill(black)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, white)
            game_display.blit(message, [display_width / 6, display_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_quit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Check for boundaries
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        game_display.fill(black)
        pygame.draw.rect(game_display, white, [food_x, food_y, snake_block_size, snake_block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        our_snake(snake_block_size, snake_list)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, display_width - snake_block_size) / 20) * 20
            food_y = round(random.randrange(0, display_height - snake_block_size) / 20) * 20
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()

# Start the game loop
game_loop()
