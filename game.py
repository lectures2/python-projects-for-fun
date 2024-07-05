import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

# Set up the game clock
clock = pygame.time.Clock()

# Player variables
player_x = width // 2
player_y = height // 2
player_speed = 5

# Mob variables
mob_radius = 20
mob_speed = 2
mob_x = random.randint(0, width - mob_radius * 2)
mob_y = random.randint(0, height - mob_radius * 2)
mob_dx = 0
mob_dy = 0

# Bullet variables
bullet_radius = 5
bullet_speed = 5
bullets = []

# Game state
playing = False
level = 1
lives = 3

def reset_game():
    global playing, player_x, player_y, mob_x, mob_y, bullets, level, lives
    playing = True
    player_x = width // 2
    player_y = height // 2
    mob_x = random.randint(0, width - mob_radius * 2)
    mob_y = random.randint(0, height - mob_radius * 2)
    bullets = []
    level = 1
    lives = 3

reset_game()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if not playing and event.key == pygame.K_SPACE:
                reset_game()
            elif event.key == pygame.K_SPACE:
                if len(bullets) < 3:  # Limit the number of bullets on the screen
                    bullets.append((player_x, player_y, mob_dx, mob_dy))
            elif event.key == pygame.K_LEFT:
                mob_dx = -mob_speed
                mob_dy = 0
            elif event.key == pygame.K_RIGHT:
                mob_dx = mob_speed
                mob_dy = 0
            elif event.key == pygame.K_UP:
                mob_dy = -mob_speed
                mob_dx = 0
            elif event.key == pygame.K_DOWN:
                mob_dy = mob_speed
                mob_dx = 0

    # Update game logic
    if playing:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Update bullet positions
        for i in range(len(bullets)):
            bullet_x, bullet_y, bullet_dx, bullet_dy = bullets[i]
            bullet_x += bullet_dx
            bullet_y += bullet_dy
            bullets[i] = (bullet_x, bullet_y, bullet_dx, bullet_dy)

        # Update mob position
        if mob_x < player_x:
            mob_x += mob_speed
        elif mob_x > player_x:
            mob_x -= mob_speed
        if mob_y < player_y:
            mob_y += mob_speed
        elif mob_y > player_y:
            mob_y -= mob_speed

        # Check collision with mob
        if (
            player_x < mob_x + mob_radius * 2
            and player_x + mob_radius * 2 > mob_x
            and player_y < mob_y + mob_radius * 2
            and player_y + mob_radius * 2 > mob_y
        ):
            lives -= 1
            if lives == 0:
                playing = False
            else:
                player_x = width // 2
                player_y = height // 2

        # Check collision between bullets and mob
        for bullet in bullets:
            bullet_x, bullet_y, _, _ = bullet
            if (
                bullet_x < mob_x + mob_radius * 2
                and bullet_x + bullet_radius * 2 > mob_x
                and bullet_y < mob_y + mob_radius * 2
                and bullet_y + bullet_radius * 2 > mob_y
            ):
                reset_game()

        # Level up if mob is killed
        if (
            mob_x < player_x + mob_radius * 2
            and mob_x + mob_radius * 2 > player_x
            and mob_y < player_y + mob_radius * 2
            and mob_y + mob_radius * 2 > player_y
        ):
            level += 1
            if level <= 30:
                mob_x = random.randint(0, width - mob_radius * 2)
                mob_y = random.randint(0, height - mob_radius * 2)

    # Draw to the screen
    screen.fill((0, 0, 0))
    if playing:
        pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, mob_radius * 2, mob_radius * 2))
        pygame.draw.rect(screen, (0, 255, 0), (mob_x, mob_y, mob_radius * 2, mob_radius * 2))
        for bullet_x, bullet_y, _, _ in bullets:
            pygame.draw.circle(screen, (0, 0, 255), (bullet_x + bullet_radius, bullet_y), bullet_radius)
        for i in range(lives):
            pygame.draw.ellipse(screen, (255, 0, 0), (10 + i * 40, height - 40, 30, 30))
        font = pygame.font.Font(None, 24)
        level_text = font.render("Level: " + str(level), True, (255, 255, 255))
        screen.blit(level_text, (10, 10))
    else:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over. Press SPACE to play again.", True, (255, 255, 255))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)

    # Update the screen
    pygame.display.flip()
    clock.tick(60)
