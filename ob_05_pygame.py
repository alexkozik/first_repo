import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Создание ракеток и мяча
left_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)

# Основная функция игры
def main():
    clock = pygame.time.Clock()
    ball_speed_x = BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Движение ракеток
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += PADDLE_SPEED
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED

        # Движение мяча
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Отскок мяча от стенок
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y = -ball_speed_y
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed_x = -ball_speed_x

        # Отскок мяча от ракеток
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_speed_x = -ball_speed_x

        # Отрисовка
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
