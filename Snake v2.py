import pygame
pygame.init()
import random


BlockSize = 15
FoodColor = [0, 255, 255]
BgColor = [0, 0, 0]

clock = pygame.time.Clock()
FPS = 60

class Block:
    
    def __init__(self, color, pos):
        self.color = color
        self.rect = pygame.Rect(pos, (BlockSize, BlockSize))
        pygame.draw.rect(screen, self.color, self.get_screen_pos())

        
    def get_screen_pos(self):
        return [[self.rect.x * BlockSize, self.rect.y * BlockSize], self.rect.size]

    def hide(self):
        pygame.draw.rect(screen, BgColor, self.get_screen_pos())


def generate_food():
    x = random.randint(0, screen_size[0] // BlockSize)
    y = random.randint(0, screen_size[1] // BlockSize)
    pos_correct = True
    for block in snake:
        if block.rect.x == x and block.rect.y == y:
            pos_correct = False
            break
    if pos_correct:
        return Block(FoodColor, (x, y))
    else:
        generate_food()


pygame.display.set_caption("Snake")
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
screen.fill(BgColor)

count = 0

hardcore_mode = False
snake_color = [255, 255, 255]
DIR = 'left'
snake = [Block(snake_color, (30, 15)), Block(snake_color, (31, 15)), Block(snake_color, (32, 15))]

food = generate_food()

running = True

while running:

    pygame.display.flip()
    count += 1

    if count % 10 == 0:

        head = snake[0]
        if DIR == 'down':
            new_head = Block(snake_color, (head.rect.x, head.rect.y + 1))
        elif DIR == 'up':
            new_head = Block(snake_color, (head.rect.x, head.rect.y - 1))
        elif DIR == 'left':
            new_head = Block(snake_color, (head.rect.x - 1, head.rect.y))
        else:
            new_head = Block(snake_color, (head.rect.x + 1, head.rect.y))

        snake.insert(0, new_head)

        if snake[0].rect == food.rect:
            food = generate_food()
        else:
            snake[-1].hide()
            snake.pop(-1)

    if hardcore_mode:
        if random.random() <= 0.3:
            snake_color = [255, 255, 255]
        else:
            snake_color = [0, 0, 0]



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_DOWN:
                DIR = "down"
            
            if event.key == pygame.K_UP:
                DIR = "up"
                
            if event.key == pygame.K_LEFT:
                DIR = "left"
                
            if event.key == pygame.K_RIGHT:
                DIR = "right"

    for i in range(1, len(snake)):
        if snake[i].rect == snake[0]:
            pygame.quit()
            running = False

    if 0 > snake[0].rect.y or snake[0].rect.y * BlockSize > screen_size[
        1] or 0 > snake[0].rect.x or snake[0].rect.x * BlockSize > screen_size[0]:
        pygame.quit()
        running = False

    clock.tick(FPS)
