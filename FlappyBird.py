import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Параметры птицы
bird_x = 50
bird_y = HEIGHT // 2
bird_size = 30
bird_speed_y = 0
gravity = 0.5
jump_height = -10

# Параметры препятствий
pipe_width = 70
pipe_gap = 150
pipe_speed = 5
pipe_x = WIDTH
pipe_height_top = random.randint(100, HEIGHT - pipe_gap - 100)
pipe_height_bottom = HEIGHT - pipe_gap - pipe_height_top

# Игровой цикл
running = True
clock = pygame.time.Clock()

# Счет
score = 0
font = pygame.font.SysFont("comicsansms", 30)

def draw_objects():
    screen.fill(WHITE)  # Заливка фона
    pygame.draw.rect(screen, BLUE, (bird_x, bird_y, bird_size, bird_size))  # Птица
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, pipe_width, pipe_height_top))  # Верхняя труба
    pygame.draw.rect(screen, GREEN, (pipe_x, HEIGHT - pipe_height_bottom, pipe_width, pipe_height_bottom))  # Нижняя труба
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def detect_collision():
    # Проверка столкновения с верхней и нижней границами экрана
    if bird_y < 0 or bird_y + bird_size > HEIGHT:
        return True
    # Проверка столкновения с трубами
    if pipe_x < bird_x + bird_size < pipe_x + pipe_width:
        if bird_y < pipe_height_top or bird_y + bird_size > HEIGHT - pipe_height_bottom:
            return True
    return False

while running:
    # Проверка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed_y = jump_height  # Птица подпрыгивает при нажатии пробела

    # Применение гравитации и изменение положения птицы
    bird_speed_y += gravity
    bird_y += bird_speed_y

    # Движение труб
    pipe_x -= pipe_speed
    if pipe_x + pipe_width < 0:
        pipe_x = WIDTH
        pipe_height_top = random.randint(100, HEIGHT - pipe_gap - 100)
        pipe_height_bottom = HEIGHT - pipe_gap - pipe_height_top
        score += 1  # Увеличение счета при прохождении трубы

    # Отрисовка объектов
    draw_objects()
    print(pipe_x)

    # Проверка на столкновения
    if detect_collision():
        running = False

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)

# Завершение Pygame 
pygame.quit()

# Вывод финального счета
print(f"Игра окончена. Ваш счет: {score}")
