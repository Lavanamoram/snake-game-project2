import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (0, 255, 0)

# Snake settings
snake_block = 20
snake_speed = 5

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, PINK, (x, y, snake_block, snake_block))

def message(msg, color):
    font_style = pygame.font.SysFont(None, 50)
    rendered_msg = font_style.render(msg, True, color)
    screen.blit(rendered_msg, (SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3))

def game_loop():
    game_over = False
    game_close = False

    # Initialize the starting position of the snake
    snake_list = []
    length_of_snake = 1
    snake_x = SCREEN_WIDTH / 2
    snake_y = SCREEN_HEIGHT / 2
    snake_x_change = 0
    snake_y_change = 0

    # Initialize the position of the food
    food_x = round(random.randrange(0, SCREEN_WIDTH - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / snake_block) * snake_block

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_block
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_block
                    snake_x_change = 0

        if snake_x >= SCREEN_WIDTH or snake_x < 0 or snake_y >= SCREEN_HEIGHT or snake_y < 0:
            game_close = True

        snake_x += snake_x_change
        snake_y += snake_y_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, (food_x, food_y, snake_block, snake_block))
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)

        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / snake_block) * snake_block
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
